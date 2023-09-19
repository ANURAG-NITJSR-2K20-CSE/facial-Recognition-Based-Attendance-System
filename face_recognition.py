from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from attendance_dashboard import Attendance
import csv
from train import Train
import datetime as dt
import sys

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition Syestem")

        title_lbl=Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #  first image
        img_top=Image.open("Image/face_recog1.jpg")
        img_top=img_top.resize((650,700), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)


        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        img_bottom=Image.open("Image/face_recog2.jpg")
        img_bottom=img_bottom.resize((950,700), Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)


        f_lbl=Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)


        # button
        b1_1=Button(f_lbl, text="Press To Recognize the face",command=self.face_recog,cursor="hand2",font=("times new roman", 12, "bold"), bg="darkgreen",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)

        back_1=Button(f_lbl, text="Back",command=self.iExit,cursor="hand2",font=("times new roman", 12, "bold"), bg="red",fg="white")
        back_1.place(x=650,y=620,width=200,height=40)

        attendance=Button(f_lbl, text="Get Attendance Data",command=self.attendance_data,cursor="hand2",font=("times new roman", 12, "bold"), bg="Orange",fg="white")
        attendance.place(x=650,y=560,width=200,height=40)

    #===========attendance in db ===================================
    def mark_attendance_in_db(self,id):
        # Connect to the database
        db = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Anurag@123",
            database="face_recognizer"
        )
        cursor = db.cursor()
        
        curr_date = dt.datetime.today().strftime('%Y-%m-%d')
        #fetch current time
        #****************** curr_sub *********************************
        date = dt.datetime.now()
        curr_day = date.strftime("%A")
        curr_sub = "No Class"

        cursor.execute("SELECT * FROM Timetable WHERE day_of_week = %s", (curr_day,))
        today_subject = cursor.fetchone()
        print(today_subject)
   
        if today_subject :
            cursor.execute("SELECT * FROM Timetable WHERE id = %s", (1,))
            period_time = cursor.fetchone()

            for i in range (2,len(period_time)):
                start_time_str , end_time_str = period_time[i].split(" - ")

                start_time = dt.datetime.strptime(start_time_str, '%I:%M %p')
                end_time = dt.datetime.strptime(end_time_str, '%I:%M %p')        
                print(start_time.time(),date.time(), end_time.time())
                if start_time.time() <= date.time() <= end_time.time():
                    curr_sub=today_subject[i]
                    break
            if curr_sub == "No Class" :
                messagebox.showerror("Error", "No class now")
                db.close()
                return
        else :
            messagebox.showerror("Error", "No class today")
            db.close()
            return
        
        # ********************************** Insert row first time **********************************

        sql = "SELECT count(*) FROM "+str(curr_sub)+" WHERE date = %s"
        cursor.execute(sql,(curr_date,))
        status = cursor.fetchone()

        if status[0] == 0:
            sql = "INSERT INTO "+str(curr_sub)+" (date"
            for i in range(1, 125):
                sql += ", roll_" + str(i)
            sql += ", sum) VALUES (%s"
            for i in range(125):
                sql += ", %s"
            sql += ")"

            value = [0] * 126
            value[0] = curr_date

            cursor.execute(sql,(value))

        # ********************************** UPDATE **********************************

        # cursor.execute("SELECT column_name FROM table_name WHERE id = 1")
        sql = "SELECT roll_"+str(id)+" FROM "+str(curr_sub)+" WHERE date = %s"
        cursor.execute(sql,(curr_date,))
        status = cursor.fetchone()

        if status[0] == 0:
            cursor.execute("SET SQL_SAFE_UPDATES=0")

            # Make attendance
            sql = "UPDATE "+str(curr_sub)+" SET roll_" + str(id) + " = %s WHERE date = %s"
            cursor.execute(sql,(1,curr_date))

            # update in that row
            sql = "UPDATE "+str(curr_sub)+" SET sum = sum + 1 WHERE date = %s"
            cursor.execute(sql,(curr_date,))

            # update in that column
            sql = "UPDATE "+str(curr_sub)+" SET roll_"+str(id)+" = roll_"+str(id)+" + 1 WHERE id = 1"
            cursor.execute(sql)

            # update total 
            sql = "UPDATE "+str(curr_sub)+" SET sum = sum + 1 WHERE id = 1"
            cursor.execute(sql)

            messagebox.showinfo("Success", "Attendance marked successfully")

            cursor.execute("SET SQL_SAFE_UPDATES=1")
        else :
            messagebox.showerror("Error", "Attendance already marked")

        db.commit()
        db.close()
                
    #==========face recognition===============================
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) 
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Anurag@123",database="face_recognizer")  
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                # my_cursor.execute("select Dep from student where Student_id="+str(id))
                my_cursor.execute("select Dep from student where Student_id="+str(id,))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id,))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                if confidence>77:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                    # cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # self.mark_attendance(i,r,n,d)
                    self.mark_attendance_in_db(r)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3) 
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h] 

            return coord
        
       
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)    
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        # clf=cv2.face.createLBPHFaceRecognizer()
        # clf=cv2.face.createEigenFaceRecognizer()


        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)
 
            if cv2.waitKey(1)==13:
               break
        video_cap.release()
        cv2.destroyAllWindows()    
    

    def iExit(self):
        self.root.destroy()
        return
    
    def attendance_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Attendance(self.new_windows)

if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop() 
