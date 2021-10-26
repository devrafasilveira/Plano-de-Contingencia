from tkinter import *
from datetime import datetime

class ScreenRegister:
    def __init__(self, master, choicefarm):
        self.master = master
        self.choicefarm = choicefarm
# Font =====================================================================
        self.font = "Poppins 14 bold"
        self.font2 = "Poppins 13 bold"
        self.fg = "#2CA6CE"
# Image BG =================================================================       
        self.imgRegister = PhotoImage(file='img/data-register.png')
        self.mainImage = Label(master, image=self.imgRegister)
        self.mainImage.pack()
# Image Farm =============================================================== 
        self.imageFarm(master, choicefarm)
# ID =======================================================================
        self.idFrame = Frame(master)
        self.idFrame.place(x=790, y=93)
        # self.idEntry = Entry(self.idFrame, borderwidth=0, fg=self.fg, width=2, font=self.font)
        # self.idEntry.pack()
        self.idLabel = Label(self.idFrame, text="12", bg='white', borderwidth=0, fg=self.fg, width=3, font=self.font)
        self.idLabel.pack()
# Room =====================================================================
        self.roomVar = StringVar()
        self.roomLabel = Label(master, textvariable=self.roomVar, width=3, height=1, borderwidth=0, bg='white', fg=self.fg, font=self.font2)
        self.roomVar.set("Nº")
        self.roomLabel.bind('<Button-1>', lambda e, var = self.roomVar: self.choiceroom(e, var))
        self.roomLabel.place(x=143, y=146)
# Professional =============================================================
        self.profVar = StringVar()
        self.profLabel = Label(master, textvariable=self.profVar, width=13, height=1, borderwidth=0, bg='white', fg=self.fg, font=self.font2)
        self.profVar.set("Escolha")
        self.profLabel.bind('<Button-1>', lambda e, var = self.profVar: self.choiceprofessional(e, var))
        self.profLabel.place(x=395, y=146)
# Registry =================================================================
        self.regFrame = Frame(master)
        self.regFrame.place(x=730, y=144)
        self.regLabel = Label(self.regFrame, bg='white', fg=self.fg, width=8, font=self.font)
        self.regLabel.pack()
# Date/Hour ================================================================
        self.dateFrame = Frame(master)
        self.dateFrame.place(x=203, y=205)
        self.dateEntry = Entry(self.dateFrame, borderwidth=0, fg=self.fg, width=18, font=self.font)
        datenow = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        self.dateEntry.insert(0, datenow)
        self.dateEntry.pack()
# BarCodes =================================================================
        self.bc1Frame = Frame(master)
        self.bc1Frame.place(x=124, y=317)
        self.bc1Entry = Entry(self.bc1Frame, borderwidth=0, fg=self.fg, width=25, font=self.font)
        self.bc1Entry.pack()
#==============================================
        self.bc2Frame = Frame(master)
        self.bc2Frame.place(x=124, y=363)
        self.bc2Entry = Entry(self.bc2Frame, borderwidth=0, fg=self.fg, width=25, font=self.font)
        self.bc2Entry.pack()
#==============================================
        self.bc3Frame = Frame(master)
        self.bc3Frame.place(x=124, y=409)
        self.bc3Entry = Entry(self.bc3Frame, borderwidth=0, fg=self.fg, width=25, font=self.font)
        self.bc3Entry.pack()
#==============================================
        self.bc4Frame = Frame(master)
        self.bc4Frame.place(x=124, y=455)
        self.bc4Entry = Entry(self.bc4Frame, borderwidth=0, fg=self.fg, width=25, font=self.font)
        self.bc4Entry.pack()
# Quantirity ===============================================================
        self.qtr1Frame = Frame(master)
        self.qtr1Frame.place(x=518, y=317)
        self.qtr1Entry = Entry(self.qtr1Frame, borderwidth=0, fg=self.fg, width=3, font=self.font)
        self.qtr1Entry.pack()
#==============================================
        self.qtr2Frame = Frame(master)
        self.qtr2Frame.place(x=518, y=363)
        self.qtr2Entry = Entry(self.qtr2Frame, borderwidth=0, fg=self.fg, width=3, font=self.font)
        self.qtr2Entry.pack()
#==============================================
        self.qtr3Frame = Frame(master)
        self.qtr3Frame.place(x=518, y=409)
        self.qtr3Entry = Entry(self.qtr3Frame, borderwidth=0, fg=self.fg, width=3, font=self.font)
        self.qtr3Entry.pack()
#==============================================
        self.qtr4Frame = Frame(master)
        self.qtr4Frame.place(x=518, y=455)
        self.qtr4Entry = Entry(self.qtr4Frame, borderwidth=0, fg=self.fg, width=3, font=self.font)
        self.qtr4Entry.pack()
#===================================================================================================
        self.imgNew = PhotoImage(file='img/button-new.png')
        self.btnNew = Button(master, image=self.imgNew, border=0, bg='white')
        self.btnNew.place(x=684, y=277)

        self.imgSave = PhotoImage(file='img/button-save.png')
        self.btnSave = Button(master, image=self.imgSave, border=0, bg='white')
        self.btnSave.place(x=684, y=326)

        self.imgConsult = PhotoImage(file='img/button-consult.png')
        self.btnConsult = Button(master, image=self.imgConsult, border=0, bg='white')
        self.btnConsult.place(x=684, y=375)

        self.imgClose = PhotoImage(file='img/button-close.png')
        self.btnClose = Button(master, image=self.imgClose, border=0, bg='white', command=master.destroy)
        self.btnClose.place(x=684, y=424)

    def imageFarm(self, root, choice):
        if 'uti' in choice:
            self.imgUti = PhotoImage(file='img/button-uti.png')
            self.utiLabel = Label(root, image=self.imgUti, border=0, bg='white')
            self.utiLabel.place(x=172, y=90)
        elif 'central' in choice:
            self.imgCentral = PhotoImage(file='img/button-central.png')
            self.centralLabel = Label(root, image=self.imgCentral, border=0, bg='white')
            self.centralLabel.place(x=172, y=90)
        elif 'emergency' in choice:
            self.imgEmergency = PhotoImage(file='img/button-emergency.png')
            self.emergencyLabel = Label(root, image=self.imgEmergency, border=0, bg='white')
            self.emergencyLabel.place(x=172, y=90)
