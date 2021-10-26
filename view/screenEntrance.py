from tkinter import *

class ScreenEntrance:
    def __init__(self, master):
        self.imgEntrance = PhotoImage(file='img/entrance-screen.png')
        self.mainImage = Label(master, image=self.imgEntrance) 
        self.mainImage.pack()
# Font =====================================================================
        self.font = "Poppins 14 bold"
        self.font2 = "Poppins 13 bold"
        self.fg = "#2CA6CE"
# Login ====================================================================
        self.userFrame = Frame(master)
        self.userFrame.place(x=192, y=270)
        self.userEntry = Entry(self.userFrame, borderwidth=0, fg=self.fg, width=20, font=self.font)
        self.userEntry.pack()
        self.userEntry.focus()

        self.passFrame = Frame(master)
        self.passFrame.place(x=192, y=318)
        self.passEntry = Entry(self.passFrame, show='*', borderwidth=0, fg=self.fg, width=20, font=self.font)
        self.passEntry.pack()
        self.userEntry.focus()
# Buttons ==================================================================
        self.imgBtn = PhotoImage(file='img/button-enter.png')
        self.btnEnter = Button(master, image=self.imgBtn, border=0, bg='white')
        self.btnEnter.place(x=148, y=471)

        self.imgUti = PhotoImage(file='img/button-uti.png')
        self.btnUti = Button(master, image=self.imgUti, border=0, bg='white')
        self.btnUti.place(x=167, y=411)

        self.imgCentral = PhotoImage(file='img/button-central.png')
        self.btnCentral = Button(master, image=self.imgCentral, border=0, bg='white')
        self.btnCentral.place(x=223, y=411)

        self.imgEmergency = PhotoImage(file='img/button-emergency.png')
        self.btnEmergency = Button(master, image=self.imgEmergency, bg='white', border=0)
        self.btnEmergency.place(x=317, y=411)

        self.imgRecover = PhotoImage(file='img/button-recover.png')
        self.btnRecover = Button(master, image=self.imgRecover, bg='white', border=0)
        self.btnRecover.place(x=329, y=359)

        self.imgRegister = PhotoImage(file='img/button-register.png')
        self.btnRegister = Button(master, image=self.imgRegister, bg='white', border=0)
        self.btnRegister.place(x=221, y=523)