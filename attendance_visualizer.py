import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Read the attendance data from a CSV file
df = pd.read_csv('attendance.csv')

# Count the number of present and absent students
num_present = len(df[df['Status'] == 'Present'])
num_absent = 121-len(df[df['Status'] == 'Absent'])

# Create a Tkinter window
window = tk.Tk()
window.title('Attendance Visualizer')

# Create a bar graph of attendance data
fig, ax = plt.subplots()
ax.bar(['Present', 'Absent'], [num_present, num_absent], color=['green', 'red'])
ax.set_ylabel('Number of Students')
ax.set_title('Attendance')

# Display the graph in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
window.mainloop()
