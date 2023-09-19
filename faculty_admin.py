from PIL import Image, ImageTk
from tkinter import *
import customtkinter as ctk
from train import Train
from attendance_dashboard import Attendance
from face_recognition import Face_Recognition
import cv2
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import sys
sys.path.append(
    "c:/users/anura/appdata/local/programs/python/python38/lib/site-packages")


# root=tk.Tk()
# style = ttk.Style(root)
# root.tk.call("Source","forest-light.tcl")
# root.tk.call("Source","forest-.tcl")


class Faculty:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition Syestem")

        # ==============variables==============
        self.var_sub = StringVar()
        self.var_id = StringVar()
        self.var_f_id = StringVar()
        self.var_f_name = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_pass = StringVar()

        # # title of software
        # bg_img=Label(self.root, image=self.photoimg4)
        bg_img = ctk.CTkLabel(self.root, width=1530, height=710)

        bg_img.place(x=0, y=40)

        title_lbl = Label(bg_img, text="FACULTY INFORMATION DETAILS", font=(
            "Calibri", 45, "bold"), bg="#163b06", fg="#e6f2e1")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1500, height=640)

    #    flat sunken raised groove ridge
        # left label frame
        Left_frame = LabelFrame(main_frame, relief=RIDGE, bd=4,
                                text="Faculty Details", foreground="green", bg="yellow")
        Left_frame.place(x=30, y=40, width=800, height=520)

        # class Student Information
        class_student_frame = LabelFrame(
            Left_frame, relief=RIDGE, text="Faculty information")
        class_student_frame.place(x=5, y=10, width=780, height=450)

        # faculty information

        Id_label = ttk.Label(
            class_student_frame, text="Id:", bootstyle="dark")
        Id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        ID_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_id, width=20, bootstyle="default")
        ID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        fid_label = ttk.Label(
            class_student_frame, text="Faculty Id:", bootstyle="dark")
        fid_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        fid_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_f_id, width=20, bootstyle="default")
        fid_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # student name
        studentName_label = ttk.Label(
            class_student_frame, text="Faculty Name:", bootstyle="black")
        studentName_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        StudentName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_f_name, width=20, bootstyle="black")
        StudentName_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # phone no
        phone_label = ttk.Label(class_student_frame,
                                text="Phone No:", bootstyle="black")
        phone_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_phone, width=20, bootstyle="black")
        phone_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = ttk.Label(class_student_frame,
                                text="Email:", bootstyle="black")
        email_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_email, width=20, bootstyle="black")
        email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Address
        address_label = ttk.Label(
            class_student_frame, text="Password:", bootstyle="black")
        address_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_pass, width=20, bootstyle="black")
        address_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # subject Name
        professor_label = ttk.Label(
            class_student_frame, text="Subject:", bootstyle="black")
        professor_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        professor_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_sub, width=20, bootstyle="black")
        professor_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        btn_frame = Frame(class_student_frame, bd=2, relief="flat", bg="white")
        btn_frame.place(x=0, y=300, width=545, height=35)

        save_btn = ttk.Button(
            btn_frame, text="Save", bootstyle="success", command=self.add_data, width=17)
        save_btn.grid(row=0, column=0, padx=5)

        update_btn = ttk.Button(
            btn_frame, text="Update", bootstyle="warning", command=self.update_data, width=17)
        update_btn.grid(row=0, column=1, padx=5)

        delete_btn = ttk.Button(
            btn_frame, text="delete", bootstyle="danger", command=self.delete_data, width=17)
        delete_btn.grid(row=0, column=2, padx=5)

        reset_btn = ttk.Button(
            btn_frame, text="Reset", bootstyle="secondary", command=self.reset_data, width=17)
        reset_btn.grid(row=0, column=3, padx=5)

        btn_frame2 = Frame(class_student_frame, bd=2,
                           relief="flat", bg="white")
        btn_frame2.place(x=0, y=350, width=545, height=35)

        back_btn = ttk.Button(btn_frame2, text="Back",
                              command=self.iExit, width=18, bootstyle="info")
        back_btn.grid(row=0, column=3, padx=190)

        # Right label frame
        right_frame=LabelFrame(main_frame, bd=2,bg="gray1",relief=RIDGE, text="Faculty Details",font=("times new roman", 12,"bold"))
        right_frame.place(x=600,y=10,width=885,height=550)

        # img_right=Image.open(r"Image\group.png")
        # img_right=img_right.resize((900,210), Image.LANCZOS)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(right_frame, image=self.photoimg_right)
        # f_lbl.place(x=5,y=0,width=900,height=210)

        # # ===================Search System =====================

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
        table_frame.place(x=5,y=20,width=880,height=500)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="dark-round")
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL,bootstyle="dark-round")

        # self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photos"),bootstyle="dark",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        self.student_table=ttk.Treeview(table_frame,column=("id","faculty_id","faculty_name","phone_no","Email","Password","subject"),bootstyle="dark",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # ----------------

        # ----------------

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="Id")
        self.student_table.heading("faculty_id",text="Faculty Id")
        self.student_table.heading("faculty_name",text="Faculty Name")
        self.student_table.heading("phone_no",text="Phone No")
        self.student_table.heading("Email",text="Email Id")
        self.student_table.heading("Password",text="password")
        self.student_table.heading("subject",text="Subject")

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.column("id",width=100)
        self.student_table.column("faculty_id",width=100)
        self.student_table.column("faculty_name",width=100)
        self.student_table.column("phone_no",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Password",width=100)
        self.student_table.column("subject",width=100)


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
        if self.var_id.get() == "" or self.var_f_name.get() == "" or self.var_f_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Anurag@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into faculty values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_id.get(),
                    self.var_f_id.get(),
                    self.var_f_name.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_pass.get(),
                    self.var_sub.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "success", "Faculty Details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error"f"Due To :{str(es)}", parent=self.root)

    # ======================fetch data========================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Anurag@123", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from faculty")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ==================get cursor==================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0])
        self.var_f_id.set(data[1])
        self.var_f_name.set(data[2])
        self.var_phone.set(data[3])
        self.var_email.set(data[4])
        self.var_sub.set(data[6])
        self.var_pass.set(data[5])
        

    # ====================update function==============
    def update_data(self):
        if self.var_f_id.get() == "" or self.var_f_name.get() == "" or self.var_sub.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                Upadate = messagebox.askyesno(
                    "Upadte", "Do you want to update this student details", parent=self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Anurag@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                 #    ("update student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s"
                    my_cursor.execute("update faculty SET Faculty_Id=%s,Faculty_Name=%s,Phone_No=%s,Email=%s,Password=%s,Subject=%s where id=%s", (

                        self.var_f_id.get(),
                        self.var_f_name.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_pass.get(),
                        self.var_sub.get(),
                        
                        # self.var_gender.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo(
                    "Success", "Faculty details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # delete function

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Faculty_id id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student delete page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Anurag@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from faculty where id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Sucessfully deleted facultyt details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # reset function
    def reset_data(self):
  
        self.var_id.set(""),
        self.var_f_id.set(""),
        self.var_f_name.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_pass.set(""),
        self.var_sub.set("")

    # ========generate data set or take photo Samples==================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Anurag@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s", (

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
                    self.var_std_id.get() == id+1
                ))
                conn.commit()  # connection update
                self.fetch_data()
                self.reset_data()
                conn.close()

                # =====load predefined data on face frontals from opencv===========

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.1, 6)
                    # scaling factor = 1.3
                    # minimum neighbour = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(1)  # 1 other camera
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face,)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:  # 100 sample
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating datasets completed!!!")
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    def iExit(self):
        self.root.destroy()
        return

    def face_data(self):
        self.new_windows = Toplevel(self.root)
        self.app = Face_Recognition(self.new_windows)

    def attendance_data(self):
        self.new_windows = Toplevel(self.root)
        self.app = Attendance(self.new_windows)

    def train_data(self):
        self.new_windows = Toplevel(self.root)
        self.app = Train(self.new_windows)


if __name__ == "__main__":
    root = Tk()
    obj = Faculty(root)

    root.mainloop()
