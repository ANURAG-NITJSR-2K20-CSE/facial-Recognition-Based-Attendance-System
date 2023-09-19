from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import os
from student_dashboard import Student
from train import Train
from face_recognition import Face_Recognition
from attendance_dashboard import Attendance
import time
from faculty_admin import Faculty
import subprocess

class Admin:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition Syestem")

        # bg image
        img4=Image.open("Image/nitjsr.jpg")
        img4=img4.resize((1530,850), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        # title of software
        bg_img=Label(self.root, image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=850)

        title_lbl=Label(bg_img, text="FACE RECOGNITION BASED ATTENDANCE SYSTEM",font=("times new roman", 40, "bold"), bg="#2D2727",fg="red")
        title_lbl.place(x=-5,y=-5,width=1530,height=50)
        
        # Right label frame
        right_frame=LabelFrame(bg_img)
        right_frame.place(x=900,y=45,width=630,height=800)

        #Add student details
        b0=Button(right_frame, text="Add Student Details",command=self.add_student_details,bd=5,relief=RIDGE,cursor="hand2",font=("times new roman", 15, "bold"),width=35, bg="#3C2317",fg="white")
        b0.grid(row=0,column=0,padx=100,pady=(50,10),sticky=W)

        #update student details
        b1=Button(right_frame, text="Update/Remove Student Details",command=self.update_student_details,bd=5,relief=RIDGE,cursor="hand2",font=("times new roman", 15, "bold"),width=35, bg="#3C2317",fg="white")
        b1.grid(row=1,column=0,padx=100,pady=10,sticky=W)

        #Add faculty details
        b2=Button(right_frame, text="Add Faculty Details",command=self.add_faculty_details,bd=5,relief=RIDGE,cursor="hand2",font=("times new roman", 15, "bold"),width=35, bg="#3C2317",fg="white")
        b2.grid(row=2,column=0,padx=100,pady=10,sticky=W)

        #update faculty details
        b3=Button(right_frame, text="Update/Remove Faculty Details",command=self.update_faculty_details,bd=5,relief=RIDGE,cursor="hand2",font=("times new roman", 15, "bold"),width=35, bg="#3C2317",fg="white")
        b3.grid(row=3,column=0,padx=100,pady=10,sticky=W)

        # train the dataset system
        b4=Button(right_frame, text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman", 15, "bold"),width=35, bg="#3C2317",bd=5,fg="white")
        b4.grid(row=4,column=0,padx=100,pady=10,sticky=W)
        
        # photos
        b5=Button(right_frame, text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"),width=35, bg="#3C2317",bd=5,fg="white")
        b5.grid(row=5,column=0,padx=100,pady=10,sticky=W)

        # Time Table
        b6=Button(right_frame, text="Time Table",cursor="hand2",command=self.time_table,font=("times new roman", 15, "bold"),width=35, bg="#3C2317",bd=5,fg="white")
        b6.grid(row=6,column=0,padx=100,pady=10,sticky=W)

        # Show Report
        b7=Button(right_frame, text="Show Report",cursor="hand2",command=self.show_report,font=("times new roman", 15, "bold"),width=35,height=3, bg="#3C2317",bd=5,fg="white")
        b7.grid(row=7,column=0,padx=100,pady=40,sticky=W)
        
        # exit button
        b8=Button(right_frame, text="Exit",cursor="hand2",command=self.exit,font=("times new roman", 15, "bold"),width=15, bg="#3C2317",fg="white")
        b8.place(x=400,y=700)

    # ===========================Function button==========
    def add_student_details(self):
        self.new_windows=Toplevel(self.root)
        self.app=Student(self.new_windows)

    def update_student_details(self):
        self.new_windows=Toplevel(self.root)
        self.app=Student(self.new_windows)

    def add_faculty_details(self):
        self.new_windows=Toplevel(self.root)
        self.app=Faculty(self.new_windows)

    def update_faculty_details(self):
        self.new_windows=Toplevel(self.root)
        self.app=Faculty(self.new_windows)

    def train_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Train(self.new_windows)
    
    def open_img(self):
        os.startfile("data")  

    def time_table(self):
        subprocess.call(["python", "timetable.py"])
       
    def show_report(self):
        self.new_windows=Toplevel(self.root)
        self.app=Train(self.new_windows)

    def exit(self):
        self.root.destroy()
       

if __name__== "__main__":
    # root=Tk()
    root=tk.Tk()
    obj=Admin(root)
    # style = ttk.Style(root)
    # root.tk.call("source","forest-light.tcl")
    # root.tk.call("source","forest-dark.tcl")
    # style.theme_use("forest-dark")

    root.mainloop()



