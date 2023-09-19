from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import os
from student_dashboard import Student
from train import Train
from face_recognition import Face_Recognition
from attendance_dashboard import Attendance
import ttkbootstrap as ttk
import datetime as dt
from time import strftime
from ttkbootstrap.constants import *
import customtkinter as ctk



class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition Syestem")
        
        def my_time():
            time_string = strftime('%I:%M:%S %p') # time format 
            curr_time.config(text=time_string)
            curr_time.after(1000,my_time) # time delay of 1000 milliseconds 
        
        # bg image
        img4=Image.open("Image/nitjsr.jpg")
        img4=img4.resize((1530,850), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        # # 
        # label = ctk.CTkLabel(master=root, text="CTkLabel")
        # label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # # 
        # title of software
        bg_img=Label(self.root, image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=850)

        title_lbl=Label(bg_img, text="FACE RECOGNITION BASED ATTENDANCE SYSTEM",font=("times new roman", 40, "bold"), bg="#2D2727",fg="red")
        title_lbl.place(x=-5,y=-5,width=1530,height=70)
        
        #left Label frame
        left_frame=LabelFrame(bg_img, bd=2,bg="gray1",relief=RIDGE)
        left_frame.place(x=10,y=100,width=500,height=640)

        #logo
        img1=Image.open(r"Image\logo.png").resize((200,250), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(left_frame, image=self.photoimg1)
        f_lbl.grid(row=0,column=0,columnspan=2,padx=130,pady=40,sticky=W)

        date = dt.datetime.now()

        #Date
        date_label=Label(left_frame, text="Date\t\t:",font=("times new roman", 18,"bold"))
        date_label.grid(row=1,column=0,padx=20,pady=5,sticky=W)

        curr_date = Label(left_frame, text=f"{date:%d %B %Y}", fg="white", bg="black", font=("helvetica", 18))
        curr_date.grid(row=1,column=1,pady=5,sticky=W)
        
        #Day
        day_label=ttk.Label(left_frame,text="Day\t\t:",font=("times new roman", 18,"bold"))
        day_label.grid(row=2,column=0,padx=20,pady=5,sticky=W)

        curr_day = Label(left_frame, text=f"{date:%A}", fg="white", bg="black", font=("helvetica", 18))
        curr_day.grid(row=2,column=1,pady=5,sticky=W)
        
        #Time
        day_label=ttk.Label(left_frame,text="Time\t\t:",font=("times new roman", 18,"bold"))
        day_label.grid(row=3,column=0,padx=20,pady=5,sticky=W)

        curr_time=tk.Label(left_frame,font=("helvetica",18))
        curr_time.grid(row=3,column=1,pady=5,sticky=W)
        my_time()

        #Subject
        sub_label=Label(left_frame,text="Subject\t\t:",font=("times new roman", 18,"bold"))
        sub_label.grid(row=4,column=0,padx=20,pady=5,sticky=W)

        curr_sub=Label(left_frame,text="Compiler Design",font=("helvetica",18))
        curr_sub.grid(row=4,column=1,pady=5,sticky=W)

        #Semester
        sem_label=Label(left_frame,text="Semester\t\t:",font=("times new roman", 18,"bold"))
        sem_label.grid(row=5,column=0,padx=20,pady=5,sticky=W)

        curr_sem=Label(left_frame,text="6th",font=("helvetica",18))
        curr_sem.grid(row=5,column=1,pady=5,sticky=W)
        
        #Attend
        attend_label=Label(left_frame,text="Attend\t\t:",font=("times new roman", 18,"bold"))
        attend_label.grid(row=6,column=0,padx=20,pady=5,sticky=W)

        curr_attend=Label(left_frame,text="85/121",font=("helvetica",18))
        curr_attend.grid(row=6,column=1,pady=5,sticky=W)
        
        # detect face button
        img6=Image.open("Image/facialRec.png").resize((360,350), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img, image=self.photoimg6,command=self.face_data,bg="#3C2317",cursor="hand2")
        b1.place(x=600,y=100,width=360,height=350)
        
        b1_1=Button(bg_img, text="Make Attendance",command=self.face_data,cursor="hand2",bd=5,bg="#3C2317",font=("times new roman", 30, "bold"),fg="white")
        b1_1.place(x=600,y=420,width=360,height=60)
             
        # ===================Search System =====================

        search_frame=LabelFrame(bg_img, bd=2,bg="lightyellow",relief=RIDGE, text="Search System",font=("times new roman", 12,"bold"))
        search_frame.place(x=550,y=550,width=610,height=190)

        search_label=Label(search_frame,text="Registration Number :",font=("times new roman", 13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
          
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman", 13,"bold"))
        search_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        showAll_btn=Button(search_frame,text="Show",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=2,padx=4)
       
        # login as admin
        b1_1=Button(bg_img, text="Login As Admin",cursor="hand2",font=("times new roman", 15, "bold"), bg="#3C2317",fg="white")
        b1_1.place(x=1050,y=80,width=220,height=40) 
        
        # login as Faculty
        b1_1=Button(bg_img, text="Login As Faculty",cursor="hand2",font=("times new roman", 15, "bold"), bg="#3C2317",fg="white")
        b1_1.place(x=1280,y=80,width=220,height=40) 
       
        # about page :
        imga=Image.open("Image/about.png").resize((450,350), Image.LANCZOS)
        self.photoimga=ImageTk.PhotoImage(imga)

        ba=Button(bg_img, image=self.photoimga,bg="#3C2317",cursor="hand2")
        ba.place(x=1050,y=150,width=450,height=350)
       
        # exit button
        img12=Image.open("Image/R.png").resize((220,220), Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img, image=self.photoimg12,cursor="hand2",command=self.exit, bg="#3C2317")
        b1.place(x=1250,y=550,width=150,height=150)

        b1_1=Button(bg_img, text="Exit",cursor="hand2",command=self.exit,font=("times new roman", 25, "bold"), bg="#3C2317",fg="white")
        b1_1.place(x=1250,y=700,width=150,height=40) 
   
    # ===========================Function button==========
    def face_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Face_Recognition(self.new_windows)   

    def exit(self):
        self.root.destroy()
    

if __name__== "__main__":
    root=tk.Tk()
    obj=Face_Recognition_System(root)
    # style = ttk.Style(root)
    # root.tk.call("source","forest-light.tcl")
    # root.tk.call("source","forest-dark.tcl")
    # style.theme_use("forest-dark")

    root.mainloop()



#include <bits/stdc++.h>
