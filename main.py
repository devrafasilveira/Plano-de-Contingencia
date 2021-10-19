from tkinter import *
from view.screenEntrance import ScreenEntrance
from controller.entranceController import EntranceController

root = Tk()
screenEntrance = ScreenEntrance(root)
entranceController = EntranceController(screenEntrance)
root.title('Contingenciamento Emergencial - Hospital Python')
root.resizable(width=False, height=False)
root.iconbitmap('img/favicon.ico')
root.mainloop()

if ScreenEntrance:
    root.after(500, root.destroy)
