import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math

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
root.title("Faculty Page")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# faculty_id = sys.argv[1];
faculty_id = "1"

mycursor.execute(f"SELECT * FROM faculty WHERE faculty_id = '{faculty_id}'")
row = mycursor.fetchall()

val = tk.Label(root, text="ID : " + str(row[0][1]), font=("Arial", 20, "bold"))
val.place(x=200, y=50)

val = tk.Label(root, text="Name : " + str(row[0][2]), font=("Arial", 20, "bold"))
val.place(x=800, y=50)

val = tk.Label(root, text="Phone : " + str(row[0][3]), font=("Arial", 20, "bold"))
val.place(x=200, y=100)

val = tk.Label(root, text="Email : " + str(row[0][4]), font=("Arial", 20, "bold"))
val.place(x=800, y=100)

# ******************************* button 1 **********************************************************************

canvas1 = ""
canvas2 = ""
canvas_pie = ""
canvas_bar = ""

def show_report1():
    if canvas2 != "":
        canvas2.get_tk_widget().destroy()
    if canvas_pie != "":
        canvas_pie.get_tk_widget().destroy()
    if canvas_bar != "":
        canvas_bar.get_tk_widget().destroy()
    # Define the data
    # mycursor.execute("SELECT * FROM "+str(row[0][6])+" WHERE id = 1")
    # row = mycursor.fetchone()
    # attend = list(row)[2:-1]

    attend = [39, 15, 5, 49, 34, 8, 19, 16, 17, 24, 29, 31, 38, 47, 20, 27, 
              32, 23, 49, 20, 37, 17, 7, 31, 35, 13, 37, 4, 42, 25, 2, 15, 24, 41, 17, 18, 30, 13, 4, 
              49, 50, 2, 20, 39, 36, 37, 14, 14, 50, 7, 23, 34, 18, 29, 47, 44, 6, 33, 8, 3, 21, 38, 9, 
              22, 50, 2, 37, 50, 30, 36, 48, 12, 35, 28, 8, 5, 31, 5, 3, 26, 29, 12, 28, 38, 49, 18, 23, 
              45, 25, 26, 44, 25, 34, 44, 4, 4, 33, 43, 38, 5, 46, 50, 48, 10, 22, 36, 9, 2, 39, 43, 33, 
              46, 1, 12, 18, 20, 15, 17, 13, 16, 50, 17, 20, 43]

    x_values = [i + 1 for i in range(len(attend))]  # Add 1 to each element

    # Create the figure and axis objects
    fig = Figure(figsize=(15, 6), dpi=100)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.2, left=0.1, right=0.9, top=0.9)

    # Create the bar graph
    avg_attend = sum(attend) / len(attend)

    colors = ['red' if value < 10 else 'black' if value < avg_attend else 'blue' for value in attend]
    ax.bar(x_values, attend, color=colors)

    ax.axhline(y=avg_attend, color='g', linestyle='--')
    ax.text(x=0.9, y=max(attend)+1, s=f'Average = {avg_attend:.1f}', va='center', ha='left', color='black', transform=ax.get_yaxis_transform(),bbox=dict(facecolor='red', edgecolor='none', boxstyle='round,pad=0.2'))

    # Add y-values above each bar
    for x, y in zip(x_values, attend):
        ax.text(x, y + 1, str(y), ha='center')

    # Add a title
    ax.set_title('Attendance')

    # Add axis labels
    ax.set_xlabel('Roll Number')
    ax.set_ylabel('Number of Class present')

    # Add the matplotlib canvas to the window
    global canvas1
    canvas1 = FigureCanvasTkAgg(fig, master=report_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack()

# ************************************* button 2 ****************************************************************

def show_report2():
    if canvas1 != "":
        canvas1.get_tk_widget().destroy()
    if canvas_pie != "":
        canvas_pie.get_tk_widget().destroy()
    if canvas_bar != "":
        canvas_bar.get_tk_widget().destroy()
    # Define the data
    # mycursor.execute("SELECT * FROM "+str(row[0][6])+" WHERE id = 1")
    # row = mycursor.fetchone()
    # attend = list(row)[2:-1]

    # # Define the data
    attend = [39, 15, 5, 49, 34, 8, 19, 16, 17, 24, 29, 31, 38, 47, 20, 27, 32, 23, 49, 20, 37, 17, 7, 31, 35, 13, 37, 4, 42, 25, 2, 15, 24, 41, 17, 18, 30, 13, 4, 49, 50, 2, 20, 39, 36, 37, 14, 14, 50, 7, 23, 34, 18, 29, 47, 44, 6, 33, 8, 3, 21, 38, 9, 22, 50, 2, 37, 50, 30, 36, 48, 12, 35, 28, 8, 5, 31, 5, 3, 26, 29, 12, 28, 38, 49, 18, 23, 45, 25, 26, 44, 25, 34, 44, 4, 4, 33, 43, 38, 5, 46, 50, 48, 10, 22, 36, 9, 2, 39, 43, 33, 46, 1, 12, 18, 20, 15, 17, 13, 16, 50, 17, 20, 43]

    # mycursor.execute("SELECT count(*) FROM "+str(row[0][6])+" WHERE id = 1")
    # val = mycursor.fetchone()
    # max_value = val[0] - 1

    max_value = 50  # fetch from db total number of class

    labels = ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50',
              '51-55', '56-60', '61-65', '66-70', '71-75', '76-80', '81-85', '86-90', '91-95', '96-100']

    percentages = [0] * 20
    for a in attend:
        percentage = (a / max_value) * 100
        index = percentage / 5
        if index and int(index)==index :
            index -=1
        percentages[int(index)] += 1

    # Create the figure and axis objects
    fig = Figure(figsize=(15, 6), dpi=100)
    ax = fig.add_subplot(111)

    # Create the bar graph
    ax.bar(labels, percentages,color='purple')
    for x, y in zip(labels, percentages):
        ax.text(x, y+0.03 , str(y), ha='center')

    # Add a title
    ax.set_title('Attendance')

    # Add axis labels
    ax.set_xlabel('Attendance %')
    ax.set_ylabel('Number of Students')
    ax.set_xticklabels(labels, rotation=30, ha='right',rotation_mode='anchor')

    # Add the matplotlib canvas to the window
    global canvas2
    canvas2 = FigureCanvasTkAgg(fig, master=report_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack()
    
# ************************************* button 3 ****************************************************************

def show_report3():
    if canvas1 != "":
        canvas1.get_tk_widget().destroy()
    if canvas2 != "":
        canvas2.get_tk_widget().destroy()
    ##selct first row from curr_sub table
    # mycursor.execute('SELECT date, sum FROM '+str(row[0][6]))
    # rows = mycursor.fetchall()[1:]

    # date = []
    # total_present = []

    # for row in rows:
    #     total_present.append(str(row[1]))
    #     a=str(row[0])
    #     year = a.split('-')[0].strip()
    #     month = a.split('-')[1].strip()
    #     day = a.split('-')[2].strip()
    #     date.append("{}/{}/{}".format(day, month, year))

    # mycursor.close()
    # mydb.close()

    date = ["2/4/2023","5/4/2023","7/4/2023","8/4/2023","9/4/2023","10/4/2023","12/4/2023","14/4/2023","16/4/2023","17/4/2023"]
    total_present = [67,98,54,79,120,34,27,95,35,75]

    avg = sum(total_present) / len(total_present)

    #********* Bar Chart *******

    fig = Figure(figsize=(10,6), dpi=100)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.2)

    colors = ['red' if value < avg else 'blue' for value in total_present]
    ax.bar(date, total_present, color=colors)

    ax.axhline(y=avg, color='g', linestyle='--')
    ax.text(x=0.8, y=max(total_present)+1, s=f'Average = {avg:.1f}', va='center', ha='left', color='black', transform=ax.get_yaxis_transform(),bbox=dict(facecolor='yellow', edgecolor='none', boxstyle='round,pad=0.2'))

    # Add y-values above each bar
    for x, y in zip(date, total_present):
        ax.text(x, y + 1, str(y), ha='center')

    ax.set_title('Attendance')
    ax.set_xlabel('Date')
    ax.set_xticklabels(date, rotation=30)
    ax.set_ylabel('Number of Students present')

    #******* pie chart **********

    greater = len([x for x in total_present if x >= avg])
    smaller = len(total_present)-greater

    fig_pie = Figure(figsize=(5,6), dpi=100)
    ax_pie = fig_pie.add_subplot(111)
    fig_pie.subplots_adjust(left=0.2, right=0.7)

    ax_pie.pie([greater, smaller], labels=['More than Avg.', 'Less than Avg.'], autopct='%1.1f%%', startangle=90)
    ax_pie.set_title('Attendance')

    #******* GUI ************
    # Add the matplotlib canvas to the window
    global canvas_bar
    canvas_bar = FigureCanvasTkAgg(fig, master=report_frame)
    canvas_bar.draw()
    canvas_bar.get_tk_widget().grid(row=0, column=0)

    global canvas_pie
    canvas_pie = FigureCanvasTkAgg(fig_pie, master=report_frame)
    canvas_pie.draw()
    canvas_pie.get_tk_widget().grid(row=0, column=1)


#***************************** button to add a new student ****************************************************
add_student = ctk.CTkButton(root, text=" All Student ",command=show_report1, font=("Arial", 20, "bold"))
add_student.place(x=200, y=170)

add_student = ctk.CTkButton(root, text=" Percentage Wise ",command=show_report2, font=("Arial", 20, "bold"))
add_student.place(x=400, y=170)

add_student = ctk.CTkButton(root, text=" Date Wise ",command=show_report3, font=("Arial", 20, "bold"))
add_student.place(x=650, y=170)

report_frame = ctk.CTkFrame(root, width=1400, height=550)
report_frame.place(x=70, y=220)
show_report1()

root.mainloop()