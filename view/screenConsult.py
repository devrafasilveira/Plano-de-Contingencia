from tkinter import *
from tkinter import ttk

class ScreenConsult:
    def __init__(self, master=None):
# Font =====================================================================
        self.font = "Poppins 14 bold"
        self.fg = "#2CA6CE"
# Image BG =================================================================   
        self.imgConsult = PhotoImage(file='img/data-consult.png')
        self.labelConsult = Label(master, image=self.imgConsult)
        self.labelConsult.pack()
# ID =======================================================================
        self.idFrame = Frame(master)
        self.idFrame.place(x=669, y=87)
        self.idEntry = Entry(self.idFrame, borderwidth=0, fg=self.fg, width=2, font=self.font)
        self.idEntry.pack()
# Room =====================================================================
        self.roomFrame = Frame(master)
        self.roomFrame.place(x=141, y=139)
        self.roomEntry = Entry(self.roomFrame, borderwidth=0, fg=self.fg, width=2, font=self.font)
        self.roomEntry.pack()
# Professional =============================================================
        self.profFrame = Frame(master)
        self.profFrame.place(x=379, y=139)
        self.profEntry = Entry(self.profFrame, borderwidth=0, fg=self.fg, width=12, font=self.font)
        self.profEntry.pack()
# Registry =================================================================
        self.regFrame = Frame(master)
        self.regFrame.place(x=730, y=139)
        self.regEntry = Entry(self.regFrame, borderwidth=0, fg=self.fg, width=7, font=self.font)
        self.regEntry.pack()
# Date/Hour ================================================================
        self.dateFrame = Frame(master)
        self.dateFrame.place(x=203, y=200)
        self.dateEntry = Entry(self.dateFrame, borderwidth=0, fg=self.fg, width=16, font=self.font)
        self.dateEntry.pack()
# BarCodes =================================================================
        self.bc1Frame = Frame(master)
        self.bc1Frame.place(x=124, y=312)
        self.bc1Entry = Entry(self.bc1Frame, borderwidth=0, fg=self.fg, width=23, font=self.font)
        self.bc1Entry.pack()
#==============================================
        self.bc2Frame = Frame(master)
        self.bc2Frame.place(x=124, y=358)
        self.bc2Entry = Entry(self.bc2Frame, borderwidth=0, fg=self.fg, width=23, font=self.font)
        self.bc2Entry.pack()
#==============================================
        self.bc3Frame = Frame(master)
        self.bc3Frame.place(x=124, y=404)
        self.bc3Entry = Entry(self.bc3Frame, borderwidth=0, fg=self.fg, width=23, font=self.font)
        self.bc3Entry.pack()
#==============================================
        self.bc4Frame = Frame(master)
        self.bc4Frame.place(x=124, y=450)
        self.bc4Entry = Entry(self.bc4Frame, borderwidth=0, fg=self.fg, width=23, font=self.font)
        self.bc4Entry.pack()
# Qtds =====================================================================
        self.qtd1Frame = Frame(master)
        self.qtd1Frame.place(x=518, y=312)
        self.qtd1Entry = Entry(self.qtd1Frame, borderwidth=0, fg=self.fg, width=3, font=self.font)
        self.qtd1Entry.pack()
#==============================================
        self.qtd2Frame = Frame(master)
        self.qtd2Frame.place(x=518, y=358)
        self.qtd2Entry = Entry(self.qtd2Frame, borderwidth=0, fg=self.fg, width=3, font=self.font)
        self.qtd2Entry.pack()
#==============================================
        self.qtd3Frame = Frame(master)
        self.qtd3Frame.place(x=518, y=404)
        self.qtd3Entry = Entry(self.qtd3Frame, borderwidth=0, fg=self.fg, width=3, font=self.font)
        self.qtd3Entry.pack()
#==============================================
        self.qtd4Frame = Frame(master)
        self.qtd4Frame.place(x=518, y=450)
        self.qtd4Entry = Entry(self.qtd4Frame, borderwidth=0, fg=self.fg, width=3, font=self.font)
        self.qtd4Entry.pack()
#===================================================================================================
        self.imgConsult2 = PhotoImage(file='img/button-consult2.png')
        self.btnConsult2 = Button(master, image=self.imgConsult2, border=0, bg='white')
        self.btnConsult2.place(x=720, y=85)

        self.imgRecicle = PhotoImage(file='img/button-recicle.png')
        self.btnRecicle  = Button(master, image=self.imgRecicle, border=0, bg='white')
        self.btnRecicle .place(x=684, y=375)

        self.imgBack = PhotoImage(file='img/button-back.png')
        self.btnBack = Button(master, image=self.imgBack, border=0, bg='white', command=master.destroy)
        self.btnBack.place(x=684, y=424)