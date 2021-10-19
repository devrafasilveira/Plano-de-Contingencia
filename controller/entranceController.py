from tkinter import *
from controller.newUserController import NewUserController
from controller.recoverController import RecoverController
from model.entrance import Entrance
from model.entranceDB import EntranceDB
from view.screenNewUser import ScreenNewUser
from view.screenRecover import ScreenRecover
from view.screenRegister import ScreenRegister
from controller.registerController import RegisterController
from model.database import Database

db = Database()
ok = db.connect()

class EntranceController:
    def __init__(self, screenEntrance):
        self.choicefarm = []
        self.screenentrance = screenEntrance
        self.screenentrance.btnEnter['command'] = self.eventBtnEnter
        self.screenentrance.btnUti['command'] = self.eventBtnUti
        self.screenentrance.btnCentral['command'] = self.eventBtnCentral
        self.screenentrance.btnEmergency['command'] = self.eventBtnEmergency
        self.screenentrance.btnRegister['command'] = self.eventBtnRegister
        self.screenentrance.btnRecover['command'] = self.eventBtnRecover

    def eventBtnEnter(self):
        user = self.screenentrance.userEntry.get()
        password = self.screenentrance.passEntry.get()

        entrance = Entrance(user, password)
        entranceDB = EntranceDB(db.connection)
        insertOk = entranceDB.consultDate(entrance)
        if insertOk:
            pass
        else:
            self.msgErro = Label(text='Login ou Senha errado', font='Poppins 9 bold', bg='white', fg='red', pady=0) 
            self.msgErro.place(x=235, y=452)
            self.msgErro.after(1000, lambda: self.msgErro.destroy()) 

        if len(self.choicefarm) == 0:
            self.msgErro = Label(text='Escolha uma farmácia', font='Poppins 9 bold', bg='white', fg='red', pady=0) 
            self.msgErro.place(x=235, y=452)
            self.msgErro.after(1000, lambda: self.msgErro.destroy()) 
        elif len(self.choicefarm) > 1:
            self.msgErro2 = Label(text='Escolha SOMENTE uma farmácia', font='Poppins 9 bold', bg='white', fg='red') 
            self.msgErro2.place(x=167, y=427)  
            self.msgErro2.after(1000, lambda: self.msgErro2.destroy())                      
        else:
            self.window = Toplevel()
            self.window.title('Serviço de Farmácia - Registro')
            self.window.resizable(width=False, height=False)
            self.window.iconbitmap('img/favicon.ico') 
            self.screenregister = ScreenRegister(self.window, self.choicefarm)
            self.registerController = RegisterController(self.screenregister, self.choicefarm)
            mainloop()

    def eventBtnUti(self):
        self.choicefarm.append('uti')
        self.img = PhotoImage(file='img/button-uti2.png')
        self.btn = Button(image=self.img, border=0, bg='white', command=lambda: self.btn.place_forget())
        self.btn.bind('<ButtonPress-1>', lambda event:self.choicefarm.remove('uti'))
        self.btn.place(x=167, y=411)
        mainloop()

    def eventBtnCentral(self):
        self.choicefarm.append('central')
        self.img2 = PhotoImage(file='img/button-central2.png')
        self.btn2 = Button(image=self.img2, border=0, bg='white', command=lambda: self.btn2.place_forget())
        self.btn2.bind('<ButtonPress-1>', lambda event:self.choicefarm.remove('central'))
        self.btn2.place(x=223, y=411)
        mainloop()

    def eventBtnEmergency(self):
        self.choicefarm.append('emergency')
        self.img3 = PhotoImage(file='img/button-emergency2.png')
        self.btn3 = Button(image=self.img3, border=0, bg='white', command=lambda: self.btn3.place_forget())
        self.btn3.bind('<ButtonPress-1>', lambda event:self.choicefarm.remove('emergency'))
        self.btn3.place(x=317, y=411)
        mainloop()

    def eventBtnRecover(self):
        self.window = Toplevel()
        self.window.title('Serviço de Farmácia - Recuperação de Senha')
        self.window.resizable(width=False, height=False)
        self.window.iconbitmap('img/favicon.ico') 
        self.screenrecover = ScreenRecover(self.window)
        self.recoverController = RecoverController(self.screenrecover)
        mainloop()   

    def eventBtnRegister(self):
        self.window = Toplevel()
        self.window.title('Serviço de Farmácia - Cadastro')
        self.window.resizable(width=False, height=False)
        self.window.iconbitmap('img/favicon.ico') 
        self.screennewuser = ScreenNewUser(self.window)
        self.newuserController = NewUserController(self.screennewuser)
        mainloop()   