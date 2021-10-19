from tkinter import *
from model.database import Database
from tkinter.messagebox import showinfo 
from model.recover import Recover
from model.recoverDB import RecoverDB

db = Database()
ok = db.connect()

class RecoverController:
    def __init__(self, screenRecover):
        self.screenrecover = screenRecover
        self.screenrecover.btnRegister['command'] = self.eventBtnRegister

    def eventBtnRegister(self):
        user = self.screenrecover.userEntry.get()
        password = self.screenrecover.passEntry.get()
        r_password = self.screenrecover.r_passEntry.get()

        recover = Recover(user, password, r_password)
        recoverDB = RecoverDB(db.connection)
        insertOk = recoverDB.updateDate(recover)
        if insertOk:
            showinfo('Serviço de Farmácia - Cadastro', 'Dados atualizados com sucesso')
            # list = contingencyDb.listRegistry()
            # root = Tk()
            # candidatesList = CandidatesList(root, len(list), list)
            # root.mainloop()
        else:
            showinfo('Serviço de Farmácia - Cadastro', 'Problemas no cadastro')
