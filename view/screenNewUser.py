from tkinter import *

class ScreenNewUser:
    def __init__(self, master):
        self.imgRegistry = PhotoImage(file='img/registry.png')
        self.mainImage = Label(master, image=self.imgRegistry) 
        self.mainImage.pack()
# Font =====================================================================
        self.font = "Poppins 14 bold"
        self.font2 = "Poppins 13 bold"
        self.fg = "#2CA6CE"
# Name =====================================================================
        self.nameFrame = Frame(master)
        self.nameFrame.place(x=75, y=123)
        self.nameEntry = Entry(self.nameFrame, borderwidth=0, fg=self.fg, width=20, font=self.font)
        self.nameEntry.pack()
# Registry =================================================================
        self.regFrame = Frame(master)
        self.regFrame.place(x=75, y=198)
        self.regEntry = Entry(self.regFrame, borderwidth=0, fg=self.fg, width=20, font=self.font)
        self.regEntry.pack()
# User =====================================================================
        self.userFrame = Frame(master)
        self.userFrame.place(x=75, y=273)
        self.userEntry = Entry(self.userFrame, borderwidth=0, fg=self.fg, width=20, font=self.font)
        self.userEntry.pack()
# Password =================================================================
        self.passFrame = Frame(master)
        self.passFrame.place(x=75, y=348)
        self.passEntry = Entry(self.passFrame, show="*", borderwidth=0, fg=self.fg, width=20, font=self.font)
        self.passEntry.pack()
# R-Password================================================================
        self.r_passFrame = Frame(master)
        self.r_passFrame.place(x=75, y=424)
        self.r_passEntry = Entry(self.r_passFrame, show="*", borderwidth=0, fg=self.fg, width=20, font=self.font)
        self.r_passEntry.pack()
# Button1 ==================================================================
        self.imgRegister = PhotoImage(file='img/button-newregister.png')
        self.btnRegister = Button(master, image=self.imgRegister, bg='white', border=0)
        self.btnRegister.place(x=381, y=375)
# Button2 ==================================================================
        self.imgBack = PhotoImage(file='img/button-back.png')
        self.btnBack = Button(master, image=self.imgBack, bg='white', border=0, command=master.destroy)
        self.btnBack.place(x=381, y=424)