import tkinter as tk
from PIL import Image, ImageTk

class ImageSlider(tk.Frame):
    def __init__(self, parent, image_files):
        tk.Frame.__init__(self, parent)
        self.image_files = image_files
        self.current_image_index = 0
        self.create_widgets()
        
    def create_widgets(self):
        self.image_label = tk.Label(self)
        self.image_label.pack()
        
        self.prev_button = tk.Button(self, text="Prev", command=self.show_prev_image)
        self.prev_button.pack(side="left")
        
        self.next_button = tk.Button(self, text="Next", command=self.show_next_image)
        self.next_button.pack(side="right")
        
        self.show_image()
        
    def show_image(self):
        image_file = self.image_files[self.current_image_index]
        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
    def show_next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
        self.show_image()
        
    def show_prev_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.image_files)
        self.show_image()

root = tk.Tk()

# Define an initial list of image files
initial_image_files = ["fr1.jpg", "fr.png", "Image/logo.png"]
slider = ImageSlider(root, initial_image_files)
slider.pack()

# Update the list of image files
# updated_image_files = ["image4.jpg", "image5.jpg", "image6.jpg"]
updated_image_files = ["fr.png","fr1.jpg", "logo.png"]


slider.image_files = updated_image_files

root.mainloop()
