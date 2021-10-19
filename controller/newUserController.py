from tkinter import *
from model.newUser import NewUser
from model.newUserDB import NewUserDB
from model.database import Database
from tkinter.messagebox import showinfo 

db = Database()
ok = db.connect()

class NewUserController:
    def __init__(self, screenNewUser):
        self.screennewuser = screenNewUser
        self.screennewuser.btnRegister['command'] = self.eventBtnRegister

    def eventBtnRegister(self):
        name = self.screennewuser.nameEntry.get()
        registry = self.screennewuser.regEntry.get()
        user = self.screennewuser.userEntry.get()
        password = self.screennewuser.passEntry.get()
        r_password = self.screennewuser.r_passEntry.get()

        newUser = NewUser(name, registry, user, password, r_password)
        newUserDB = NewUserDB(db.connection)
        insertOk = newUserDB.insertDate(newUser)
        if insertOk:
            showinfo('Serviço de Farmácia - Cadastro', 'Dados cadastrados com sucesso')
            # list = contingencyDb.listRegistry()
            # root = Tk()
            # candidatesList = CandidatesList(root, len(list), list)
            # root.mainloop()
        else:
            showinfo('Serviço de Farmácia - Cadastro', 'Problemas no cadastro')
