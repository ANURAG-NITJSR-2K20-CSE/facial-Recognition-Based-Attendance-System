import customtkinter as ctk
from PIL import Image, ImageTk
import datetime as dt
from time import strftime
import tkinter as tk
from admin_control_panel import Admin
from tkinter import Toplevel
import subprocess
import mysql.connector
# -------------------------------------------------------------

db = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Anurag@123",
    database="face_recognizer"
)
cursor = db.cursor()


def authentcate():
    # def iExit(self):
    #     self.root.destroy()
    #     return
    def admin_page():
        # TODO: Implement the admin page
        new_windows = Toplevel(root1)
        app = Admin(new_windows)

    def login():
        # Retrieve the username and password entered by the user
        username = username_entry.get()
        password = password_entry.get()

        # Check if the username and password are correct
        if username == "1" and password == "1":
            # Redirect the user to the admin page
            # new_windows=Toplevel(root)
            # app=Admin(new_windows)
            subprocess.call(["python", "admin.py"])
            root1.destroy()
        else:
            # Show an error message if the username or password is incorrect
            error_label.config(text="Invalid username or password")

    # Create the main window
    root1 = tk.Tk()
    root1.title("Login Form")
    root1.geometry("400x300+700+400")
    root1.resizable(False, False)
    root1.configure(bg='#3253ad')

    # Create the header label
    header_label = tk.Label(root1, text="Welcome", font=(
        "Helvetica", 24, 'bold'), bg='#3253ad')
    header_label.pack(pady=10)

    # Create the username label and entry field
    username_label = tk.Label(root1, text="Username:", font=(
        "Helvetica", 12, 'bold'), bg='#3253ad')
    username_label.pack()
    username_entry = tk.Entry(root1, font=("Helvetica", 12))
    username_entry.pack(pady=5)

    # Create the password label and entry field
    password_label = tk.Label(root1, text="Password:", font=(
        "Helvetica", 12, 'bold'), bg='#3253ad')
    password_label.pack()
    password_entry = tk.Entry(root1, show="*", font=("Helvetica", 12))
    password_entry.pack(pady=5)

    # Create the login button
    login_button = tk.Button(root1, text="Login", command=login,
                             bg='#3253ad', fg='white', font=("Helvetica", 12, 'bold'), padx=10)
    login_button.pack(pady=10)

    # Create the error label
    error_label = tk.Label(root1, fg="red", bg='#3253ad')
    error_label.pack()

    # Start the main loop
    root1.mainloop()

# -------------------------------------------------------------


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080+0+0")
        self.title(" ")

        img4=Image.open("Image/front_jsr.png")
        img4=img4.resize((1930,1050), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        # title of software
        bg_img=ctk.CTkLabel(self, image=self.photoimg4,width=1530,height=850 , text='')
        bg_img.place(x=0,y=0)
        # self.resizable(False,False)
        self.configure(fg_color='white', image='Image/logo.png')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)
        
        # Load the image
        # image = Image.open("image.jpg")
        # photo = ImageTk.PhotoImage(image)

        # # Create a label with the image and place it at (0,0)
        # label = tk.Label(self, image=photo)
        # label.place(x=0, y=0, relwidth=1, relheight=1)

        def my_time():
            time_string = strftime('%I:%M:%S %p')  # time format
            curr_time.configure(text=time_string)
            curr_time.after(1000, my_time)  # time delay of 1000 milliseconds

        # # add widgets to app
        # self.button = ctk.CTkButton(self, command=self.button_click)
        # self.button.grid(row=0, column=1, padx=20, pady=10)
        
        
        
        frame = ctk.CTkFrame(master=self, width=1920,
                             height=100, corner_radius=0,  fg_color='#274187')
        frame.place(x=0, y=0)
        label = ctk.CTkLabel(frame, text="Facial Recognition Based Attendance System               ", font=(
            'Arial', 50, 'bold'), fg_color='#274187', text_color='white')
        label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        frame4 = ctk.CTkFrame(master=self, width=1920, height=61,
                              corner_radius=0, border_width=0, fg_color='#3253ad')
        frame4.place(x=0, y=99)
        frame3 = ctk.CTkFrame(master=self, width=1920,
                              height=61, corner_radius=0, fg_color='#3253ad')
        frame3.place(x=1050, y=99)
        # ------------------------------------------------------------
        # frame5 = ctk.CTkFrame(master=self, width=1920, height = 640)
        # frame5.place(x=0, y=160)
        # #  Load the image
        # image = Image.open("fr.")
        # photo = ImageTk.PhotoImage(image)

        # # Create a label with the image and place it at (0,0)
        # label = tk.Label(frame5, image=photo)
        # # label.place(x=0, y=0, relwidth=1, relheight=1)
        # label.pack()
        # ---------------------------------------------------------------

        frame3.rowconfigure(0, weight=1, uniform='b')
        frame3.columnconfigure(0, weight=2, uniform='b')

        # button inside frame 3
        # about_button = ctk.CTkButton(frame3, text="About us", width=100, height=40, border_color='#57C5B6', border_width=1, hover_color='#159895',fg_color='gray20')
        # about_button.grid(row = 0, column = 0, padx=5, pady=7)

        # login_as_admin_button = ctk.CTkButton(frame3, text="Login as Admin",command=authentcate, width=50, height=40, border_color='#57C5B6', border_width=1, hover_color='#159895', fg_color='gray20')
        # login_as_admin_button.grid(row = 0, column = 1, padx=5, pady=7)

        # login_as_faculty_button = ctk.CTkButton(frame3, text="Login as Faculty", width=50, height=40, border_color='#57C5B6', border_width=1, hover_color='#159895', fg_color='gray20')
        # login_as_faculty_button.grid(row = 0, column = 2, padx=5, pady=7)

        about_button = ctk.CTkButton(frame3, text="About us", width=100, height=60, hover_color='#274187',
                                     fg_color='#3253ad', corner_radius=0, font=('Arial', 16, 'bold'))
        # about_button.grid(row = 0, column = 0, padx=5, pady=7)
        about_button.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)

        login_as_admin_button = ctk.CTkButton(frame3, text="Login as Admin", command=authentcate, width=50, height=40,
                                              border_color='#45b6fe', hover_color='#274187', fg_color='#3253ad', corner_radius=0, font=('Arial', 16, 'bold'))
        login_as_admin_button.grid(
            row=0, column=1, sticky='nsew', padx=0, pady=0, ipadx=20)

        login_as_faculty_button = ctk.CTkButton(frame3, text="Login as Faculty", width=50, height=40, border_color='#45b6fe',
                                                hover_color='#274187', fg_color='#3253ad', corner_radius=0, font=('Arial', 16, 'bold'))
        login_as_faculty_button.grid(
            row=0, column=2, sticky='nsew', padx=0, pady=0, ipadx=20)

        left_frame = ctk.CTkFrame(
            master=self, width=300, height=650, fg_color='#d9e9ff', corner_radius=0, border_width=2, border_color='blue')
        # frame.place(x=0,y=0)
        left_frame.grid(row=0, column=0, rowspan=2, pady=(100,0))

        # logo
        img1 = Image.open(r"logo.png").resize((200, 250), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = ctk.CTkLabel(left_frame, image=self.photoimg1)
        f_lbl.grid(row=0, column=0, columnspan=2, padx=130, pady=40)

        date = dt.datetime.now()

        # Date
        date_label = ctk.CTkLabel(
            left_frame, text="Date\t\t:", font=("helvetica", 18, "bold"), text_color='black')
        date_label.grid(row=1, column=0, padx=20, pady=5)

        curr_date = ctk.CTkLabel(left_frame, text=f"{date:%d %B %Y}", font=("helvetica", 18),text_color='black')
        curr_date.grid(row=1, column=1, pady=5)

        # Day
        day_label = ctk.CTkLabel(
            left_frame, text="Day\t\t:", font=("helvetica", 18, "bold"), text_color='black')
        day_label.grid(row=2, column=0, padx=20, pady=5)

        curr_day = ctk.CTkLabel(left_frame, text=f"{date:%A}", font=("helvetica", 18), text_color='black')
        curr_day.grid(row=2, column=1, pady=5)

        # Time
        day_label = ctk.CTkLabel(left_frame, text="Time\t\t:", font=(
            "helvetica", 18, "bold"), text_color='black')
        day_label.grid(row=3, column=0, padx=20, pady=5)

        curr_time = ctk.CTkLabel(
            left_frame, text_color='black', font=("helvetica", 18))
        curr_time.grid(row=3, column=1, pady=5)
        my_time()

         #Subject

        curr_day = date.strftime("%A")
        curr_subject = "No Class"

        cursor.execute("SELECT * FROM Timetable WHERE day_of_week = %s", (curr_day,))
        today_subject = cursor.fetchone()
   
        if today_subject :
            cursor.execute("SELECT * FROM Timetable WHERE id = %s", (1,))
            period_time = cursor.fetchone()

            for i in range (2,len(period_time)):
                start_time_str , end_time_str = period_time[i].split(" - ")

                start_time = dt.datetime.strptime(start_time_str, '%I:%M %p')
                end_time = dt.datetime.strptime(end_time_str, '%I:%M %p')        
                
                if start_time.time() <= date.time() <= end_time.time():
                    curr_subject=today_subject[i]
                    break
        
        db.close()

        sub_label=ctk.CTkLabel(left_frame,text="Subject\t\t:",font=("helvetica", 18,"bold"), text_color='black')
        sub_label.grid(row=4,column=0,padx=20,pady=5)

        curr_sub=ctk.CTkLabel(left_frame,text=curr_subject,font=("helvetica",18), text_color='black')
        curr_sub.grid(row=4,column=1,pady=5)

         #Semester
        sem_label=ctk.CTkLabel(left_frame,text="Semester\t\t:",font=("times new roman", 18,"bold"), text_color='black')
        sem_label.grid(row=5,column=0,padx=20,pady=5)

        curr_sem=ctk.CTkLabel(left_frame,text="6th",font=("helvetica",18),text_color='black')
        curr_sem.grid(row=5,column=1,pady=5)
        
        #Attend
        attend_label=ctk.CTkLabel(left_frame,text="Attend\t\t:",font=("helvetica", 18,"bold"), text_color='black')
        attend_label.grid(row=6,column=0,padx=20,pady=5)

        curr_attend=ctk.CTkLabel(left_frame,text="85/121",font=("helvetica",18), text_color='black')
        curr_attend.grid(row=6,column=1,pady=5)
        

        frame1 = ctk.CTkFrame(master=self, width=1920,
                              height=60, corner_radius=0)
        frame1.place(x=0, y=800)
        label1 = ctk.CTkLabel(frame1, text="Group 9 Project Made under Supervison of Dr. Mantosh Bishwas                                  ", font=(
            'Fira Code', 18, 'bold'))
        label1.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

    # add methods to app
    def button_click(self):
        print("button click")


app = App()
app.mainloop()
