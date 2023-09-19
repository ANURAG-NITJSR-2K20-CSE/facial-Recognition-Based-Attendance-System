from customtkinter import *
from customtkinter import CustomLabel, CustomEntry, CustomButton, CustomToplevel
from admin_control_panel import Admin

def admin_page():
    # TODO: Implement the admin page
    new_window = CustomToplevel(root1)
    app = Admin(new_window)

def login():
    # Retrieve the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        # Redirect the user to the admin page
        admin_page()
    else:
        # Show an error message if the username or password is incorrect
        error_label.config(text="Invalid username or password")

# Create the main window
root1 = CTk()
root1.title("Login Form")
root1.geometry("400x300")
root1.resizable(False, False)
root1.configure(bg='#57C5B6')

# Create the header label
header_label = CustomLabel(root1, text="Welcome", font=("Helvetica", 24, 'bold'), bg='#57C5B6')
header_label.pack(pady=10)

# Create the username label and entry field
username_label = CustomLabel(root1, text="Username:", font=("Helvetica", 12, 'bold'), bg='#57C5B6')
username_label.pack()
username_entry = CustomEntry(root1, font=("Helvetica", 12))
username_entry.pack(pady=5)

# Create the password label and entry field
password_label = CustomLabel(root1, text="Password:", font=("Helvetica", 12, 'bold'), bg='#57C5B6')
password_label.pack()
password_entry = CustomEntry(root1, show="*", font=("Helvetica", 12))
password_entry.pack(pady=5)

# Create the login button
login_button = CustomButton(root1, text="Login", command=login, bg='#6fa8dc', fg='white', font=("Helvetica", 12, 'bold'), padx=10)
login_button.pack(pady=10)

# Create the error label
error_label = CustomLabel(root1, fg="red", bg='#57C5B6')
error_label.pack()

# Start the main loop
root1.mainloop()
