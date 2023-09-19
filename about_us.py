import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image
# from aboutus import AboutUsFrame
root = ctk.CTk()
root.title("About Us")
root.geometry("1920x1080+0+0")
# root.configure(fg_color)


scroll_frame = ttk.Frame(root)
scroll_frame.pack(fill='both', expand=True)

canvas = tk.Canvas(scroll_frame)
canvas.pack(side='left', fill='both', expand=True)

scrollbar = ttk.Scrollbar(scroll_frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

content_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor='nw')

title_frame = ctk.CTkFrame(content_frame, width= 1920, height=200, corner_radius=0)
title_frame.pack()

about_us_label = ttk.Label(title_frame, text='About Us                    ', font=('Arial', 60, 'bold'), justify='left',foreground='red',border=0, background='gray17')
# about_us_label.pack(pady=10)
about_us_label.place(relx= 0.5, rely=0.5, anchor= ctk.CENTER)

title_frame = ctk.CTkFrame(content_frame, width= 1920, height=2000, corner_radius=0, fg_color = '#57C5B6')
title_frame.pack(side='left')

# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
# about_us_text = ttk.Label(content_frame, text=text, font=('Arial', 12), justify='left')
# about_us_text.pack(padx=20, pady=10)

# about_us_text = tk.Text(content_frame, wrap='word', font=('Arial', 12), height=10)
# about_us_text.insert('end', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel sodales enim. Sed porttitor urna et ex feugiat, nec faucibus justo bibendum. Suspendisse ullamcorper tellus id metus malesuada, vel gravida metus bibendum. Nulla sollicitudin dolor nisl, at luctus nulla consequat a. Donec euismod nulla sed felis euismod bibendum. Praesent sit amet arcu at mi pharetra semper in id elit. Quisque a massa lectus. Aliquam sit amet nulla mauris. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum nec euismod tellus. Nulla facilisi. Aliquam sed fringilla magna. Sed sagittis sapien nec nunc auctor, non iaculis eros pulvinar. Vestibulum bibendum posuere imperdiet.')

# about_us_text.config(state='disabled')
# about_us_text.pack(padx=20, pady=10)

# about_us_text = tk.Text(content_frame, wrap='word', font=('Arial', 12), height=10)
# about_us_text.insert('end', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel sodales enim. Sed porttitor urna et ex feugiat, nec faucibus justo bibendum. Suspendisse ullamcorper tellus id metus malesuada, vel gravida metus bibendum. Nulla sollicitudin dolor nisl, at luctus nulla consequat a. Donec euismod nulla sed felis euismod bibendum. Praesent sit amet arcu at mi pharetra semper in id elit. Quisque a massa lectus. Aliquam sit amet nulla mauris. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum nec euismod tellus. Nulla facilisi. Aliquam sed fringilla magna. Sed sagittis sapien nec nunc auctor, non iaculis eros pulvinar. Vestibulum bibendum posuere imperdiet.')

# about_us_text.config(state='disabled')
# about_us_text.pack(padx=20, pady=10)

# about_us_text = tk.Text(content_frame, wrap='word', font=('Arial', 12), height=10)
# about_us_text.insert('end', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel sodales enim. Sed porttitor urna et ex feugiat, nec faucibus justo bibendum. Suspendisse ullamcorper tellus id metus malesuada, vel gravida metus bibendum. Nulla sollicitudin dolor nisl, at luctus nulla consequat a. Donec euismod nulla sed felis euismod bibendum. Praesent sit amet arcu at mi pharetra semper in id elit. Quisque a massa lectus. Aliquam sit amet nulla mauris. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum nec euismod tellus. Nulla facilisi. Aliquam sed fringilla magna. Sed sagittis sapien nec nunc auctor, non iaculis eros pulvinar. Vestibulum bibendum posuere imperdiet.')

# about_us_text.config(state='disabled')
# about_us_text.pack(padx=20, pady=10)

# about_us_text = tk.Text(content_frame, wrap='word', font=('Arial', 12), height=10)
# about_us_text.insert('end', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel sodales enim. Sed porttitor urna et ex feugiat, nec faucibus justo bibendum. Suspendisse ullamcorper tellus id metus malesuada, vel gravida metus bibendum. Nulla sollicitudin dolor nisl, at luctus nulla consequat a. Donec euismod nulla sed felis euismod bibendum. Praesent sit amet arcu at mi pharetra semper in id elit. Quisque a massa lectus. Aliquam sit amet nulla mauris. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum nec euismod tellus. Nulla facilisi. Aliquam sed fringilla magna. Sed sagittis sapien nec nunc auctor, non iaculis eros pulvinar. Vestibulum bibendum posuere imperdiet.')

# about_us_text.config(state='disabled')
# about_us_text.pack(padx=20, pady=10)

# ------------------------------------------------------------------------------------------------------------------------

# Create a header label
header_label = tk.Label(title_frame, text="About Team Member", font=("Arial", 24), bg="white")
header_label.pack(pady=20)
        
# Create a container for the team member cards
team_container = tk.Frame(title_frame, bg="white")
team_container.pack(pady=20, side='left')

# Define a list of team members
team_members = [
    {
        "name": "John Smith",
        "role": "CEO and Founder",
        "photo": "Image/attend.png"
    },
    {
        "name": "Jane Doe",
        "role": "Chief Technology Officer",
        "photo": "Image/attend.png"
    },
    {
        "name": "Mark Johnson",
        "role": "Software Engineer",
        "photo": "Image/attend.png"
    },
    {
        "name": "Sarah Lee",
        "role": "Product Manager",
        "photo": "Image/attend.png"
    },
    {
        "name": "Professor Michael Brown",
        "role": "Advisor",
        "photo": "Image/attend.png"
    }
]
        
# Loop through the team members and create a card for each one
for member in team_members:
    member_card = tk.Frame(team_container, bg="white")
    member_card.pack(side="left", padx=20)
    
    # Load the member's photo and resize it
    photo = Image.open(member["photo"])
    photo = photo.resize((200, 200))
    photo_tk = ImageTk.PhotoImage(photo)
    
    # Create a label for the member's photo
    photo_label = tk.Label(member_card, image=photo_tk, bg="white")
    photo_label.image = photo_tk
    photo_label.pack(pady=10)
    
    # Create a label for the member's name
    name_label = tk.Label(member_card, text=member["name"], font=("Arial", 16), bg="white")
    name_label.pack()
    
    # Create a label for the member's role
    role_label = tk.Label(member_card, text=member["role"], font=("Arial", 12), bg="white")
    role_label.pack()

# ------------------------------------------------------------------------------------------------------------------------


root.mainloop()
