import tkinter as tk

class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("400x300")
        self.resizable(False,False)
        self.configure(bg='#57C5B6')

        # Create the header label
        self.header_label = tk.Label(self, text="Welcome", font=("Helvetica", 24, 'bold'), bg='#57C5B6')
        self.header_label.pack(pady=10)

        # Create the username label and entry field
        self.username_label = tk.Label(self, text="Username:", font=("Helvetica", 12,'bold'), bg='#57C5B6')
        self.username_label.pack()
        self.username_entry = tk.Entry(self, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)

        # Create the password label and entry field
        self.password_label = tk.Label(self, text="Password:", font=("Helvetica", 12, 'bold'), bg='#57C5B6')
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.password_entry.pack(pady=5)

        # Create the login button
        self.login_button = tk.Button(self, text="Login", command=self.login, bg='#6fa8dc', fg='white', font=("Helvetica", 12, 'bold'), padx=10)
        self.login_button.pack(pady=10)

        # Create the error label
        self.error_label = tk.Label(self, fg="red", bg='#57C5B6')
        self.error_label.pack()

    def login(self):
        # Retrieve the username and password entered by the user
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username and password are correct
        if username == "admin" and password == "password":
            # Redirect the user to the admin page
            self.admin_page()
        else:
            # Show an error message if the username or password is incorrect
            self.error_label.config(text="Invalid username or password")

    def admin_page(self):
        # TODO: Implement the admin page
        pass

if __name__ == "__main__":
    app = LoginForm()
    app.mainloop()