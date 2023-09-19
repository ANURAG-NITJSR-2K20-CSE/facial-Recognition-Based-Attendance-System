from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import customtkinter as  ctk
class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition Syestem")

        title_lbl=Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # title_label = Label(root, text="TRAIN DATASET", font=("Helvetica", 48, "bold"), fg="green", bg="#ffffff")
        # title_label.place(relx=0.5, rely=0.1, anchor=CENTER,width=1530,height=45)
        
        img_top=Image.open("Image/training2.jpeg")
        img_top=img_top.resize((1530,725), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)


        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=725)
        
        # button
        
        style = ttk.Style()
        style.theme_use('clam')

        # b1_1=ttk.Button(self.root, text="Press To Train The Data",command=self.train_classifier,style="Animated.TButton",cursor="hand2",font=("times new roman", 30, "bold"), bg="red",fg="white")
        # b1_1.place(x=250,y=380,width=500,height=50)
        
        style.map("Animated.TButton",
          foreground=[('pressed', 'white'), ('active', 'white')],
          background=[('pressed', '!disabled', 'black'), ('active', '#333333')]
          )
        
        # b1_1=ctk.CTkButton(self.root, text="Press To Train The Data",command=self.train_classifier,style="Animated.TButton",cursor="hand2")
        # b1_1.place(x=250,y=380,width=500,height=50)

        b1_1=ctk.CTkButton(self.root, text="Press To Train The Data",command=self.train_classifier,width=500,height=50,cursor="hand2")
        b1_1.place(x=250,y=380)
        # img_bottom=Image.open(r"Image\nit_logo.jpg")
        # img_bottom=img_bottom.resize((1530,325), Image.LANCZOS)
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)


        # f_lbl=Label(self.root, image=self.photoimg_bottom)
        # f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)] # list comprehension   
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grayscale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            # C:\face_recognition_system\data\user.1.1.jpg
            # 0                               1

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp) 
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ==train the classifier and save========================
        clf=cv2.face.LBPHFaceRecognizer_create()
        # clf=cv2.face.createLBPHFaceRecognizer()

        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training dataset completed!!")





if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop() 
