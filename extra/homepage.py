import customtkinter as ctk
import tkinter as tk

from tkinter import *

# from ttkthemes import ThemedStyle

from tkinter import *
from PIL import ImageTk, Image

root = ctk.CTk()
root.title(
    "                                                                                                                                                                                                         Face Recognition based Attendance System"
)


# style = ThemedStyle(root)
# style.theme_use('clam')

# Set the background color to white
root.configure(bg="white")
root.iconbitmap("Image/scan.ico")
# Get the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to the screen size
root.geometry("{}x{}+0+0".format(screen_width, screen_height))


# -------------------------------------------------------------------------------------
nav_bar = ctk.CTkFrame(root, fg_color="#FF0000", height=60, corner_radius=0)
nav_bar.pack(fill="both")

# Add a shadow effect to the frame
# style.configure('TFrame', background='white', borderwidth=10, relief='groove', bordercolor='black', padding=10, lightcolor='gray90', darkcolor='gray70')
# Run the main event loop

# --------------------------------------------------------------------------------------
dash_board = ctk.CTkFrame(
    root,
    height=400,
    width=400,
    fg_color="#F6F1F1",
    corner_radius=50,
    border_color="#FF0000",
    border_width=1.5,
)
dash_board.pack(side="left", padx=150, pady=(0, 120))

image = Image.open("Image/jsr.png").resize((215, 245))
photo = ImageTk.PhotoImage(image)

label = ctk.CTkLabel(dash_board, image=photo)
label.pack(pady=20)

framed1 = ctk.CTkFrame(dash_board, height=40, fg_color="#e8e8e8")
framed1.pack(padx=60)
date_label = ctk.CTkLabel(framed1, fg_color="gray100", corner_radius=5)
date_label.pack(padx=20, pady=4)
framed2 = ctk.CTkFrame(dash_board, height=40, fg_color="#e8e8e8")
framed2.pack(padx=30, pady=10)
framed3 = ctk.CTkFrame(dash_board, height=40, fg_color="#e8e8e8")
framed3.pack(padx=30, pady=(0, 60))


root.mainloop()
