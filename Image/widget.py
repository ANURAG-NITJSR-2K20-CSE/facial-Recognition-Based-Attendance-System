import customtkinter as ctk

from ctypes import windll, byref, sizeof, c_int


class App(ctk.CTk):
    def __init__(self):

        # main setup
        super().__init__(fg_color='#323232')
        self.title("BMI WIDGET")
        self.geometry('1080x720')
        # self.resizable(False, False)

        # self.change_title_bar_color()
        

        # --------------------------------------------------header --------------------------------------------------------------
        header = ctk.CTkFrame(self, fg_color='orange',corner_radius=0 ,height=111)
        header.pack(fill = 'x')

        header_label = ctk.CTkLabel(header, text = "FACE RECOGNITION BASED ATTENDANCE SYSTEM", font=('Arial', 40, 'bold'), text_color=  '#323232')
        header_label.pack(expand = True,fill = 'both', pady = 30 )
        # ---------------------------------------------------------------------------------------------------------------------------

        # -------------------------------------------------navigation-----------------------------------------------------------------------
        

        # -------------------------body------------------------------------------------------------
        body = ctk.CTkFrame(self, fg_color='#0D7377',corner_radius=0 ,height=111)
        body.pack(fill = 'x')
         
        dashboard = ctk.CTkFrame(body, fg_color='#06113C',corner_radius=20 ,height=400, width = 300)
        dashboard.pack(side = 'left', padx=(150, 0))

        body_label = ctk.CTkLabel(body, text = "body", font=('Arial', 40, 'bold'), text_color=  '#323232', height = 570, width = 1920)
        body_label.pack(side = 'bottom',expand = True,fill = 'both', pady = 30 )
        
        # ------------------------------------------------footer-----------------------------------------------------------------
        footer = ctk.CTkFrame(self, fg_color='black',corner_radius=0 ,height=111)
        footer.pack(fill = 'x')

        footer_label = ctk.CTkLabel(footer, text = "footer", font=('Arial', 40, 'bold'), text_color=  '#323232')
        footer_label.pack(side = 'bottom',expand = False,fill = 'both', pady = 30 )
        
        self.mainloop()




app = App()


