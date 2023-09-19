import tkinter as tk

root = tk.Tk()
root.geometry('400x400')

# Create a canvas
canvas = tk.Canvas(root, bg='white')
canvas.pack(side='left', fill='both', expand=True)

# Add a scrollbar to the canvas
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side='right', fill='y')

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Create a frame inside the canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

# Add some widgets to the frame
for i in range(20):
    tk.Label(frame, text=f'This is label {i}').grid(row=i, column=0)

root.mainloop()
