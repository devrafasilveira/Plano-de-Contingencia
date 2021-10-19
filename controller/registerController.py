from tkinter import *
from model.database import Database
from model.contingencyDb import ContingencyDb
from model.contingency import Contingency
from controller.consultController import ConsultController
from view.screenRegister import ScreenRegister
from view.screenConsult import ScreenConsult
from tkinter.messagebox import showinfo 

db = Database()
ok = db.connect()

class RegisterController:
    def __init__(self, screenRegister, choicefarm):
        self.eventChoiceProf = []
        self.regNumber = []
        self.choicefarm = choicefarm
        self.screenregister = screenRegister
        self.screenregister.btnNew['command'] = self.eventBtnNew
        self.screenregister.btnSave['command'] = self.eventBtnSave
        self.screenregister.btnConsult['command'] = self.eventBtnConsult
        self.screenregister.choiceroom = self.choiceRoom
        self.screenregister.choiceprofessional = self.choiceProfessional
        self.screenregister.idcomplete = self.eventIdComplete
        self.screenregister.regLabel['text'] = self.eventRegComplete
    
    def eventBtnNew(self):
        self.window = Toplevel()
        self.window.title('Serviço de Farmácia - Registro')
        self.window.resizable(width=False, height=False)
        self.window.iconbitmap('img/favicon.ico')
        self.screenregister = ScreenRegister(self.window, self.choicefarm)
        self.registerController = RegisterController(self.screenregister, self.choicefarm)
        mainloop()
        
    def eventBtnSave(self):
        pharmacy = self.choicefarm
        pharmacy = ''.join(pharmacy)
        room = self.screenregister.roomVar.get()
        professional = self.screenregister.profVar.get()
        registry = self.screenregister.regEntry.get()
        datetime = self.screenregister.dateEntry.get()
        barcode1 = self.screenregister.bc1Entry.get()
        barcode2 = self.screenregister.bc2Entry.get()
        barcode3 = self.screenregister.bc3Entry.get()
        barcode4 = self.screenregister.bc4Entry.get()
        quantity1 = self.screenregister.qtr1Entry.get()
        quantity2 = self.screenregister.qtr2Entry.get()
        quantity3 = self.screenregister.qtr3Entry.get()
        quantity4 = self.screenregister.qtr4Entry.get()

        contingency = Contingency(pharmacy, room, professional, registry, datetime, barcode1, barcode2, barcode3, barcode4, quantity1, quantity2, quantity3, quantity4)
        contingencyDb = ContingencyDb(db.connection)
        insertOk = contingencyDb.insertDate(contingency)
        if insertOk:
            showinfo('Serviço de Farmácia - Registro', 'Dados cadastrados com sucesso')
            # list = contingencyDb.listRegistry()
            # root = Tk()
            # candidatesList = CandidatesList(root, len(list), list)
            # root.mainloop()
        else:
            showinfo('Serviço de Farmácia - Registro', 'Problemas no cadastro')

    def eventBtnConsult(self):
        self.window = Toplevel()
        self.window.title('Serviço de Farmácia - Consulta')
        self.window.resizable(width=False, height=False)
        self.window.iconbitmap('img/favicon.ico') 
        self.screenConsult = ScreenConsult(self.window)
        self.consultController = ConsultController(self.screenConsult)
        mainloop()

    def choiceRoom(self, e, var):
        def A(var):
            var.set("01")
        def B(var):
            var.set("02")
        def C(var):
            var.set("03")
        def D(var):
            var.set("04")
        e.widget.focus()
        nclst=[('01', lambda var = var: A(var)),
                ('02', lambda var = var: B(var)),
                ('03', lambda var = var: C(var)),
                ('04', lambda var = var: D(var)),]

        my_menu = Menu(None, tearoff=0, takefocus=0)
        for (txt, cmd) in nclst:
            my_menu.add_command(label=txt, command=cmd)
        my_menu.tk_popup(e.x_root+40, e.y_root+10,entry="0")
        
    def choiceProfessional(self, e, var):
        def A(var):
            var.set("Ana")
            self.eventChoiceProf.clear()
            self.eventChoiceProf.append('Ana')
        def B(var):
            var.set("Bianca")
            self.eventChoiceProf.clear()
            self.eventChoiceProf.append('Bianca')
        def C(var):
            var.set("Cristina")
            self.eventChoiceProf.clear()
            self.eventChoiceProf.append('Cristina')
        def R(var):
            var.set("Renata")
            self.eventChoiceProf.clear()
            self.eventChoiceProf.append('Renata')
        e.widget.focus()
        nclst=[('Ana', lambda var = var: A(var)),
                ('Bianca', lambda var = var: B(var)),
                ('Cristina', lambda var = var: C(var)),
                ('Renata', lambda var = var: R(var)),]

        my_menu = Menu(None, tearoff=0, takefocus=0)
        for (txt, cmd) in nclst:
                my_menu.add_command(label=txt, command=cmd)
        my_menu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

    def eventIdComplete(self):
        contingencyDb = ContingencyDb(db.connection)
        consultOk = contingencyDb.insertId()
        return consultOk
        # if consultOk:
        #     showinfo('Plano de Contingência', 'ID cadastrado com sucesso')

    def eventRegComplete():
        return 123456            