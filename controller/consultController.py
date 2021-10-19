from tkinter import *

class ConsultController:
    def __init__(self, screenConsult):
        self.screenconsult = screenConsult
        self.screenconsult.btnConsult2['command'] = self.eventBtnConsult2
        self.screenconsult.btnRecicle['command'] = self.eventBntRecicle
        # self.screenconsult.btnBack['command'] = self.eventBtnBack

    def eventBtnConsult2(self):
        pass

    def eventBntRecicle(self):
        pass

    def eventBtnBack(self):
        pass