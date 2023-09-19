import tkinter as tk
from PIL import ImageTk, Image

class AboutUsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.configure(bg="white")
        self.pack(fill="both", expand=True)
        
        # Create a header label
        header_label = tk.Label(self, text="About Us", font=("Arial", 24), bg="white")
        header_label.pack(pady=20)
        
        # Create a container for the team member cards
        team_container = tk.Frame(self, bg="white")
        team_container.pack(pady=20)
        
        # Define a list of team members
        team_members = [
            {
                "name": "John Smith",
                "role": "CEO and Founder",
                "photo": "attend.png"
            },
            {
                "name": "Jane Doe",
                "role": "Chief Technology Officer",
                "photo": "attend.png"
            },
            {
                "name": "Mark Johnson",
                "role": "Software Engineer",
                "photo": "attend.png"
            },
            {
                "name": "Sarah Lee",
                "role": "Product Manager",
                "photo": "attend.png"
            },
            {
                "name": "Professor Michael Brown",
                "role": "Advisor",
                "photo": "attend.png"
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

# Create a main window
root1 = tk.Tk()
root1.geometry("800x600")

# # Add the About Us section to the window
# about_us_frame = AboutUsFrame(root)

# Run the main event loop
root1.mainloop()
