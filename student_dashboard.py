import sys
sys.path.append("c:/users/anura/appdata/local/programs/python/python38/lib/site-packages")

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from face_recognition import Face_Recognition
from attendance_dashboard import Attendance
from train import Train

# root=tk.Tk()
# style = ttk.Style(root)
# root.tk.call("Source","forest-light.tcl")
# root.tk.call("Source","forest-.tcl")



class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition Syestem")
    
        # ==============variables==============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        # self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        # self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        # self.var_teacher=StringVar()

        # first image
        img1=Image.open("Image/students.jpg")
        img1=img1.resize((1000,130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=ttk.Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=550,height=130)
       
        # second image
        img2=Image.open("Image/stdents2.jpg")
        img2=img2.resize((550,130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=550,y=0,width=550,height=130)

        # third image
        img3=Image.open(r"Image\nit_logo.jpg")
        img3=img3.resize((550,130), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        f_lbl=Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
                # bg image
        img4=Image.open(r"Image\attend.jpg")
        img4=img4.resize((1530,710), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        # title of software
        bg_img=Label(self.root, image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img, text="STUDENT INFORMATION DETAILS", font=("PT Serif", 35, "bold"), bg="#163b06",fg="#e6f2e1")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        

        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=5,y=55,width=1500,height=640)
        
    #    flat sunken raised groove ridge
        # left label frame
        Left_frame=LabelFrame(main_frame,relief=RIDGE, bd=4,text="Student Details",foreground="green",bg="yellow")
        Left_frame.place(x=10,y=10,width=570,height=620)
        
        # img_left=Image.open(r"Image\nit_logo.jpg")
        # img_left=img_left.resize((720,130), Image.LANCZOS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)


        # f_lbl=Label(Left_frame, image=self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=720,height=130)
    
        # current course information
        current_course_frame=ttk.LabelFrame(Left_frame, text="Current Course Information",bootstyle="black")
        current_course_frame.place(x=5,y=10,width=555,height=125)
        
        # Department
        dep_label=ttk.Label(current_course_frame,text="Department",bootstyle="dark")
        dep_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=17,state="readonly")
        dep_combo["values"]=("Select Department","CSE","ECE","ELECTRICAL","MECH","CIVIL","PI","MCA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)


        # Course
        course_label=ttk.Label(current_course_frame,text="Course",bootstyle="dark")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,bootstyle="black",state="readonly")
        course_combo["values"]=("Select Course","B.Tech","M.Tech","M.Sc")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        
        # Year
        year_label=ttk.Label(current_course_frame,text="Year",bootstyle="dark")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,bootstyle="dark",width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        # Semester
        semester_label=ttk.Label(current_course_frame,text="Semester",bootstyle="dark")
        semester_label.grid(row=1,column=2,padx=2,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,bootstyle="dark",width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # class Student Information
        class_student_frame=LabelFrame(Left_frame,relief=RIDGE, text="Class student information")
        class_student_frame.place(x=5,y=140,width=555,height=450)
        
        #student id
        studentId_label=ttk.Label(class_student_frame,text="StudentID:",bootstyle="dark")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,bootstyle="default")
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # student name
        studentName_label=ttk.Label(class_student_frame,text="Student Name:",bootstyle="black")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        StudentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,bootstyle="black")
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # # class division
        # studentName_label=ttk.Label(class_student_frame,text="Class Division:",bootstyle="dark")
        # studentName_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # StudentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,bootstyle="dark")
        # StudentName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        # div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=18,bootstyle="warning",state="dark")
        # div_combo["values"]=("A","B","C")
        # div_combo.current(0)
        # div_combo.grid(row=1,column=1,padx=10,pady=15,sticky=W)
        # Roll no
        roll_no_label=ttk.Label(class_student_frame,text="Roll No:",bootstyle="black")
        roll_no_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,bootstyle="black")
        roll_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Gender
        gender_label=ttk.Label(class_student_frame,text="Gender:",bootstyle="black")
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman", 13,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=18,bootstyle="black",state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        # Date of Birth
        # gender_dob_label=ttk.Label(class_student_frame,text="DOB:",bootstyle="black")
        # gender_dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        # gender_dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,bootstyle="black")
        # gender_dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         # Email
        email_label=ttk.Label(class_student_frame,text="Email:",bootstyle="black")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,bootstyle="black")
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         # phone no
        phone_label=ttk.Label(class_student_frame,text="Phone No:",bootstyle="black")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,bootstyle="black")
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         # Address
        address_label=ttk.Label(class_student_frame,text="Address:",bootstyle="black")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,bootstyle="black")
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #  # Professor Name
        # professor_label=ttk.Label(class_student_frame,text="Professor Name:",bootstyle="black")
        # professor_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        # professor_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,bootstyle="black")
        # professor_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        # radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",bootstyle="info",value="Yes")
        radionbtn1.grid(row=6,column=0,padx=10)
        
    
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",bootstyle="info",value="NO")
        radionbtn2.grid(row=6,column=1,padx=10)
        
       
        btn_frame=Frame(class_student_frame,bd=2,relief="flat",bg="white")
        btn_frame.place(x=0,y=300,width=545,height=35)

        save_btn=ttk.Button(btn_frame,text="Save",bootstyle="success",command=self.add_data,width=17)
        save_btn.grid(row=0,column=0,padx=5)

        update_btn=ttk.Button(btn_frame,text="Update",bootstyle="warning",command=self.update_data,width=17)
        update_btn.grid(row=0,column=1,padx=5)
        
        delete_btn=ttk.Button(btn_frame,text="delete",bootstyle="danger",command=self.delete_data,width=17)
        delete_btn.grid(row=0,column=2,padx=5)

        reset_btn=ttk.Button(btn_frame,text="Reset",bootstyle="secondary",command=self.reset_data,width=17)
        reset_btn.grid(row=0,column=3,padx=5)

        btn_frame1=Frame(class_student_frame,bd=2,relief="flat",bg="white")
        btn_frame1.place(x=0,y=335,width=545,height=35)

        take_photo_btn=ttk.Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=30,bootstyle="dark")
        take_photo_btn.grid(row=0,column=0,padx=5)

        update_photo_btn=ttk.Button(btn_frame1,text="Update Photo Sample",width=30,bootstyle="orange")
        update_photo_btn.grid(row=0,column=1,padx=5)

        train_btn=ttk.Button(btn_frame1,text="train",command=self.train_data,width=20,bootstyle="info")
        train_btn.grid(row=0,column=3,padx=5)

        btn_frame2=Frame(class_student_frame,bd=2,relief="flat",bg="white")
        btn_frame2.place(x=0,y=370,width=545,height=35)

        dynamic_btn=ttk.Button(btn_frame2,text="Dynamic Attendance",command=self.face_data,width=28,bootstyle="info")
        dynamic_btn.grid(row=0,column=1,padx=5)

        attendance_btn=ttk.Button(btn_frame2,text="Static Attendance",command=self.attendance_data,width=28,bootstyle="info")
        attendance_btn.grid(row=0,column=2,padx=5)

        back_btn=ttk.Button(btn_frame2,text="Back",command=self.iExit,width=18,bootstyle="info")
        back_btn.grid(row=0,column=3,padx=5)

        

        # Right label frame
        right_frame=LabelFrame(main_frame, bd=2,bg="gray1",relief=RIDGE, text="Student Details",font=("times new roman", 12,"bold"))
        right_frame.place(x=600,y=10,width=885,height=620)

        img_right=Image.open(r"Image\group.png")
        img_right=img_right.resize((900,210), Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)


        f_lbl=Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=900,height=210)


        
        # ===================Search System =====================

        # search_frame=LabelFrame(right_frame, bd=2,bg="lightyellow",relief=RIDGE, text="Search System",font=("times new roman", 12,"bold"))
        # search_frame.place(x=5,y=135,width=710,height=70)

        # search_label=Label(search_frame,text="Search By",font=("times new roman", 13,"bold"),bg="red",fg="white")
        # search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        # search_combo=ttk.Combobox(search_frame,font=("times new roman", 13,"bold"),width=15,state="readonly")
        # search_combo["values"]=("Select","Roll_No","Phone_No")
        # search_combo.current(0)
        # search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        
        # search_entry=ttk.Entry(search_frame,width=15,font=("times new roman", 13,"bold"))
        # search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        # search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # search_btn.grid(row=0,column=3,padx=4)

        # showAll_btn=Button(search_frame,text="Show",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # showAll_btn.grid(row=0,column=4,padx=4)
        
        # table frame ========================================================
        table_frame=Frame(right_frame, bd=2,bg="black",relief=RIDGE)
        table_frame.place(x=5,y=210,width=880,height=387)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="dark-round")
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL,bootstyle="dark-round")
        
        # self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photos"),bootstyle="dark",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","roll","gender","email","phone","address","photos"),bootstyle="dark",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # ----------------
        
        # ----------------


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        # self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        # self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        # self.student_table.heading("teacher",text="teacher")
        self.student_table.heading("photos",text="status of photo")

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        # self.student_table.column("div",width=100)
        # self.student_table.column("dob",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        # self.student_table.column("teacher",width=100)
        self.student_table.column("photos",width=150)
        
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

# ===================function decreption==========================================

    # def add_data(self):
    #    if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
    #       messagebox.showerror("Error","All Fields are required",parent=self.root)
    #    else:
    #         try:
    #             conn=mysql.connector.connect(host="localhost",username="root",password="Anurag@123",database="face_recognizer")  
    #             my_cursor=conn.cursor()
    #             my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
    #                                                                                             self.var_dep.get(),
    #                                                                                             self.var_course.get(),
    #                                                                                             self.var_year.get(),
    #                                                                                             self.var_semester.get(),
    #                                                                                             self.var_std_id.get(),
    #                                                                                             self.var_std_name.get(),
    #                                                                                             # self.var_div.get(),
    #                                                                                             self.var_roll.get(),
    #                                                                                             self.var_gender.get(),
    #                                                                                             # self.var_dob.get(),
    #                                                                                             self.var_email.get(),
    #                                                                                             self.var_phone.get(),
    #                                                                                             self.var_address.get(),
    #                                                                                             # self.var_teacher.get(),
    #                                                                                             self.var_radio1.get()
    #                                                                               ))
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo("success","Student Details has been added successfully",parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error"f"Due To :{str(es)}",parent=self.root) 


    def add_data(self):
       if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
          messagebox.showerror("Error","All Fields are required",parent=self.root)
       else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anurag@123",database="face_recognizer")  
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                # self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                # self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                # self.var_teacher.get(),
                                                                                                self.var_radio1.get()
                                                                                  ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error"f"Due To :{str(es)}",parent=self.root)    

    #======================fetch data========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anurag@123",database="face_recognizer")  
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
        conn.close()         

    # ==================get cursor==================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        # self.var_div.set(data[6])
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])
        # self.var_dob.set(data[9])
        self.var_email.set(data[8])
        self.var_phone.set(data[9])
        self.var_address.set(data[10])
        # self.var_teacher.set(data[13])
        self.var_radio1.set(data[11])

    # ====================update function==============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Upadte","Do you want to update this student details",parent=self.root)
                if  Upadate>0:
                       conn=mysql.connector.connect(host="localhost",username="root",password="Anurag@123",database="face_recognizer")  
                       my_cursor=conn.cursor()
                    #    ("update student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s"
                       my_cursor.execute("update student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    
                                                                                                                                                                                       self.var_dep.get(),
                                                                                                                                                                                       self.var_course.get(),
                                                                                                                                                                                       self.var_year.get(),
                                                                                                                                                                                       self.var_semester.get(),
                                                                                                                                                                                       self.var_std_name.get(),
                                                                                                                                                                                    #    self.var_div.get(),
                                                                                                                                                                                       self.var_roll.get(),
                                                                                                                                                                                       self.var_gender.get(),
                                                                                                                                                                                    #    self.var_dob.get(),
                                                                                                                                                                                       self.var_email.get(),
                                                                                                                                                                                       self.var_phone.get(),
                                                                                                                                                                                       self.var_address.get(),
                                                                                                                                                                                    #    self.var_teacher.get(),
                                                                                                                                                                                       self.var_radio1.get(),
                                                                                                                                                                                       self.var_std_id.get()
                                                                                                                                                                                  ))
                else: 
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root) 
                conn.commit()  
                self.fetch_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)           


    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root) 
                if delete>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="Anurag@123",database="face_recognizer")  
                     my_cursor=conn.cursor()
                     sql="delete from student where Student_id=%s"
                     val=(self.var_std_id.get(),)
                     my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()  
                conn.close()      
                messagebox.showinfo("Delete","Sucessfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # reset function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        # self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        # self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        # self.var_teacher.set(""),
        self.var_radio1.set("")

    # ========generate data set or take photo Samples==================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anurag@123",database="face_recognizer")  
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    
                                                                                                                                                                                       self.var_dep.get(),
                                                                                                                                                                                       self.var_course.get(),
                                                                                                                                                                                       self.var_year.get(),
                                                                                                                                                                                       self.var_semester.get(),
                                                                                                                                                                                       self.var_std_name.get(),
                                                                                                                                                                                    #    self.var_div.get(),
                                                                                                                                                                                       self.var_roll.get(),
                                                                                                                                                                                       self.var_gender.get(),
                                                                                                                                                                                    #    self.var_dob.get(),
                                                                                                                                                                                       self.var_email.get(),
                                                                                                                                                                                       self.var_phone.get(),
                                                                                                                                                                                       self.var_address.get(),
                                                                                                                                                                                    #    self.var_teacher.get(),
                                                                                                                                                                                       self.var_radio1.get(),
                                                                                                                                                                                       self.var_std_id.get()==id+1
                                                                                                                                                                                  ))
                conn.commit() # connection update
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                # =====load predefined data on face frontals from opencv===========

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.1,6)
                    # scaling factor = 1.3
                    #minimum neighbour = 5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(1) # 1 other camera
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))    
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face,)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100: # 100 sample
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating datasets completed!!!")    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    def iExit(self):
        self.root.destroy()
        return 
    def face_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Face_Recognition(self.new_windows)

    def attendance_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Attendance(self.new_windows) 

    def train_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Train(self.new_windows)    


if __name__== "__main__":
    root=Tk()
    obj=Student(root)

    






    root.mainloop()        