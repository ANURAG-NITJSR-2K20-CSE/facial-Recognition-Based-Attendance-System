import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime as dt

# establish a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Anurag@123",
    database="face_recognizer"
)

# create a cursor object to execute SQL commands
mycursor = mydb.cursor()

# define the Tkinter GUI
root = tk.Tk()
root.title("Timetable Input")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# set the size of the window to match the screen size
root.geometry(f"{screen_width}x{screen_height}")

top_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)
top_frame.grid(row=0, column=0, sticky="nsew")
bottom_frame.grid(row=1, column=0, sticky="nsew")

# divide the top frame into three parts vertically
top_left_frame = tk.Frame(top_frame, bg="red")
top_center_frame = tk.Frame(top_frame, bg="green")
top_right_frame = tk.Frame(top_frame, bg="blue")
top_left_frame.grid(row=0, column=0, sticky="nsew")
top_center_frame.grid(row=0, column=1, sticky="nsew")
top_right_frame.grid(row=0, column=2, sticky="nsew")

# make all the rows and columns resizeable
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)
top_frame.grid_rowconfigure(0, weight=1)

#************************************** top_left_frame *************************************************

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
selected_days = []
day_labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

heading = tk.Label(top_left_frame, text=" Select Days ", font=("Arial", 20, "bold"))
heading.grid(row=0, column=0, columnspan=15, padx=10, pady=20, sticky="ew")

# create a checkbutton for each day of the week
for i, day in enumerate(days):
    var = tk.BooleanVar()
    checkbutton = tk.Checkbutton(top_left_frame, text=day, variable=var, font=("Arial", 12, "normal"))
    checkbutton.grid(row=i+1, column=0, padx=50, pady=5, sticky="w")
    selected_days.append((day, var))

# create a button to print the selected days
def print_days():
    global day_labels
    day_labels = [day for day, var in selected_days if var.get()]

print_button = tk.Button(top_left_frame, text=" Save Selected Days ", command=print_days, font=("Arial", 13, "normal"))
print_button.grid(row=len(days)+1, column=0 ,columnspan=20,padx=10, pady=20, sticky="e")

# ************************************* top_center_frame ************************************************
period_labels = ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"]

heading = tk.Label(top_center_frame, text=" Select Periods ", font=("Arial", 20, "bold"))
heading.grid(row=0, column=0, columnspan=15, padx=10, pady=20, sticky="ew")

periods_label = tk.Label(top_center_frame, text=" Number of periods in 1 day : ",font=("Arial", 12, "normal"))
periods_label.grid(row=1, column=0, padx=5, pady=15)

periods_var = tk.Entry(top_center_frame,width=5,font=("Arial", 12, "normal"))
periods_var.grid(row=1, column=1, padx=5, pady=5)

start_vars = []
end_vars = []

def save_period_timings():
    num_periods = int(periods_var.get())

    global period_labels
    period_labels = []
    for i in range(num_periods):
        period_labels.append(f"{start_vars[3*i].get()}:{start_vars[3*i+1].get()} {start_vars[3*i+2].get()} - {end_vars[3*i].get()}:{end_vars[3*i+1].get()} {end_vars[3*i+2].get()}")

def create_period_entries():
    create_entries_button.grid_forget()
    num_periods = int(periods_var.get())

    for i in range(num_periods):
        start_label = tk.Label(top_center_frame, text=" Period {} => Start Time :".format(i+1),font=("Arial", 12, "normal"))
        start_label.grid(row=i+2, column=0, padx=5, pady=5)

        start_var = tk.StringVar(top_center_frame)
        start_hour_dropdown = ttk.Combobox(top_center_frame, textvariable=start_var, values=[str(i) for i in range(1, 13)],width=3,font=("Arial", 12, "normal"))
        start_hour_dropdown.grid(row=i+2, column=1, padx=5, pady=5)
        start_hour_dropdown.current(0)
        start_vars.append(start_var)

        start_minute_var = tk.StringVar(top_center_frame)
        start_minute_dropdown = ttk.Combobox(top_center_frame, textvariable=start_minute_var, values=[str(i).zfill(2) for i in range(0, 60, 5)],width=3,font=("Arial", 12, "normal"))
        start_minute_dropdown.grid(row=i+2, column=2, padx=5, pady=5)
        start_minute_dropdown.current(0)
        start_vars.append(start_minute_var)

        start_ampm_var = tk.StringVar(top_center_frame)
        start_ampm_dropdown = ttk.Combobox(top_center_frame, textvariable=start_ampm_var, values=["AM", "PM"],width=3,font=("Arial", 12, "normal"))
        start_ampm_dropdown.grid(row=i+2, column=3, padx=5, pady=5)
        start_ampm_dropdown.current(0)
        start_vars.append(start_ampm_var)

        end_label = tk.Label(top_center_frame, text=" End Time : ".format(i+1),font=("Arial", 12, "normal"))
        end_label.grid(row=i+2, column=4, padx=5, pady=5)

        end_var = tk.StringVar(top_center_frame)
        end_hour_dropdown = ttk.Combobox(top_center_frame, textvariable=end_var, values=[str(i) for i in range(1, 13)],width=3,font=("Arial", 12, "normal"))
        end_hour_dropdown.grid(row=i+2, column=5, padx=5, pady=5)
        end_hour_dropdown.current(0)
        end_vars.append(end_var)

        end_minute_var = tk.StringVar(top_center_frame)
        end_minute_dropdown = ttk.Combobox(top_center_frame, textvariable=end_minute_var, values=[str(i).zfill(2) for i in range(0, 60, 5)],width=3,font=("Arial", 12, "normal"))
        end_minute_dropdown.grid(row=i+2, column=6, padx=5, pady=5)
        end_minute_dropdown.current(0)
        end_vars.append(end_minute_var)

        end_ampm_var = tk.StringVar(top_center_frame)
        end_ampm_dropdown = ttk.Combobox(top_center_frame, textvariable=end_ampm_var, values=["AM", "PM"],width=3,font=("Arial", 12, "normal"))
        end_ampm_dropdown.grid(row=i+2, column=7, padx=5, pady=5)
        end_ampm_dropdown.current(0)
        end_vars.append(end_ampm_var)

    print_timings_button = tk.Button(top_center_frame, text=" Save Timings ", command=save_period_timings,font=("Arial", 12, "normal"))
    print_timings_button.grid(row=11, column=4, padx=5, pady=15)

create_entries_button = tk.Button(top_center_frame, text=" Enter ", command=create_period_entries,font=("Arial", 13, "normal"))
create_entries_button.grid(row=2, column=1, padx=5, pady=15, sticky='e')

# ************************************* top_right_frame ************************************************

heading = tk.Label(top_right_frame, text=" Select Subjects ", font=("Arial", 20, "bold"))
heading.grid(row=0, column=0, columnspan=15, padx=10, pady=20, sticky="ew")

# create a label for the number of subjects
tk.Label(top_right_frame, text=" Number of subjects : ",font=("Arial", 15, "normal")).grid(row=1, column=0, padx=5, pady=5)

# create an entry widget for the number of subjects
num_subjects_entry = tk.Entry(top_right_frame,font=("Arial", 15, "normal"))
num_subjects_entry.grid(row=1, column=1, padx=5, pady=5)

def save_timetable():
    # create a table for the timetable
    # mycursor.execute("CREATE TABLE Timetable (id INT AUTO_INCREMENT PRIMARY KEY, day_of_week VARCHAR(255), period_1 VARCHAR(255), period_2 VARCHAR(255), period_3 VARCHAR(255), period_4 VARCHAR(255), period_5 VARCHAR(255))")
    sql = "CREATE TABLE Timetable (id INT AUTO_INCREMENT PRIMARY KEY, day_of_week VARCHAR(255)"
    for i in range(1, len(period_labels)+1):
        sql += ", period_" + str(i) + " VARCHAR(255)"
    sql += ")"
    mycursor.execute(sql)

    #*********** Insert time into Database *********************************************************************
 
    # sql = "INSERT INTO Timetable (day_of_week, period_1, period_2, period_3, period_4, period_5) VALUES ('NULL', period_labels[0], period_labels[1],period_labels[2],period_labels[3],period_labels[4])"
   
    sql = "INSERT INTO Timetable (day_of_week"
    for k in range(1, len(period_labels)+1):
        sql += ", period_" + str(k)   
    sql += ") VALUES (%s"   
    for k in range(len(period_labels)):
        sql += ", %s" 
    sql+=")"

    values = ["NuLL"]
    for k in range(len(period_labels)):
        values.append(period_labels[k])

    mycursor.execute(sql, tuple(values)) 

    #******************************************************************************** 

    for i, day in enumerate(day_labels):
        values = [day]
        for j, period in enumerate(period_labels):
            dropdown = dropdowns[(i*len(period_labels))+j]
            value = dropdown.get()
            values.append(value)
       
        # sql = "INSERT INTO Timetable (day_of_week, period_1, period_2, period_3, period_4, period_5) VALUES (%s, %s, %s, %s, %s, %s)"
        
        sql = "INSERT INTO Timetable (day_of_week"
        for k in range(1, len(period_labels)+1):
            sql += ", period_" + str(k)   
        sql += ") VALUES (%s"   
        for k in range(len(period_labels)):
            sql += ", %s"   
        sql += ")"
            
        mycursor.execute(sql, tuple(values))
    mydb.commit()
    messagebox.showinfo("Timetable Input", "Timetable saved successfully!")

def create_timetable():
    create_timetable_button.grid_forget()

    # create a list to hold the subject Names
    global subject_names
    subject_names = []
    for subject_entry in subjects:
        subject_name = subject_entry.get()
        subject_names.append(subject_name) 

        # mycursor.execute("CREATE TABLE Timetable (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, roll_1 INT, roll_2 INT, roll_3 INT, roll_4 INT, roll_5 INT, sum INT)")
        sql = "CREATE TABLE "+str(subject_name)+" (id INT AUTO_INCREMENT PRIMARY KEY, date DATE"
        for i in range(1, 125):
            sql += ", roll_" + str(i) + " INT"
        sql += ", sum INT)"
        mycursor.execute(sql)   

        # sql = "INSERT INTO cc (date, roll_1, roll_2, roll_3, roll_4, roll_5, sum) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        sql = "INSERT INTO "+str(subject_name)+" (date"
        for i in range(1, 125):
            sql += ", roll_" + str(i)
        sql += ", sum) VALUES (%s"
        for i in range(125):
            sql += ", %s"
        sql += ")" 

        value = [0] * 126
        value[0] = "2023-04-15"
        mycursor.execute(sql,(value))
    
    mydb.commit()

    # create a list to hold the dropdown widgets
    global dropdowns 
    dropdowns = []

    for i, day in enumerate(day_labels):
        tk.Label(bottom_frame, text=day).grid(row=i+num_subjects+4, column=0, padx=5, pady=5)
        for j, period in enumerate(period_labels):
            tk.Label(bottom_frame, text=period).grid(row=num_subjects+3, column=j+1, padx=5, pady=5)
            dropdown = tk.StringVar(bottom_frame)
            dropdown.set(subject_names[0])
            dropdown_menu = tk.OptionMenu(bottom_frame, dropdown, *subject_names)
            dropdown_menu.grid(row=i+num_subjects+4, column=j+1, padx=5, pady=5)
            dropdowns.append(dropdown)
    
    save_timetable_button = tk.Button(bottom_frame, text=" Save Timetable ", command=save_timetable)
    save_timetable_button.grid(row=num_subjects+10, column=5, padx=5, pady=5)

# create a button to submit the number of subjects
def submit_num_subjects():
    submit_button.grid_forget()
    
    global num_subjects
    num_subjects = int(num_subjects_entry.get())
    
    global subjects
    subjects = []
   
    for i in range(num_subjects):
        subject_label = tk.Label(top_right_frame, text=" Subject {} : ".format(i+1),font=("Arial", 12, "normal"))
        subject_label.grid(row=i+2, column=0, padx=5, pady=5)
        subject_entry = tk.Entry(top_right_frame,font=("Arial", 12, "normal"))
        subject_entry.grid(row=i+2, column=1, padx=5, pady=5)
        subjects.append(subject_entry)

    global create_timetable_button 
    create_timetable_button = tk.Button(top_right_frame, text=" Create Timetable ", command=create_timetable,font=("Arial", 13, "normal"))
    create_timetable_button.grid(row=num_subjects+3, column=1, padx=5, pady=15,sticky='e')

submit_button = tk.Button(top_right_frame, text=" Enter ", command=submit_num_subjects,font=("Arial", 13, "normal"))
submit_button.grid(row=2, column=1, padx=5, pady=15, sticky='e')

root.mainloop()