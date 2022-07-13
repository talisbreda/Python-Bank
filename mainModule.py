from tkinter import *
from tkinter import messagebox

from main import authenticate
from bankModule import BankApplication
from loginModule import LoginApplication
from registerModule import RegisterApplication

class MainApplication:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.title = Label(self.widget1, bg='LightBlue', text="Bem-vindo ao banco Python!")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.registerTextContainer = Frame(self.widget1, bg='lightgreen')
        self.registerTextContainer["width"] = 100
        self.registerTextContainer["height"] = 15
        self.registerTextContainer.pack(pady=(120, 0))

        self.registerText = Label(self.registerTextContainer, text="Registre-se")
        self.registerText["font"] = ("Verdana", "10", "bold")
        self.registerText.pack(side=LEFT, pady = (0, 5))

        self.registerButton = Button(self.widget1, text="Registrar")
        self.registerButton["width"] = 15
        self.registerButton.bind("<Button-1>", self.register)
        self.registerButton.pack(pady = 15)

        self.loginTextContainer = Frame(self.widget1, bg='lightgreen')
        self.loginTextContainer["width"] = 100
        self.loginTextContainer["height"] = 15
        self.loginTextContainer.pack()

        self.loginText = Label(self.loginTextContainer, text="Login")
        self.loginText["font"] = ("Verdana", "10", "bold")
        self.loginText.pack(side=LEFT, pady = (0, 5))

        self.loginButton = Button(self.widget1, text="Login")
        self.loginButton["width"] = 15
        self.loginButton.bind("<Button-1>", self.login)
        self.loginButton.pack(pady = 15)
    
    def login(self, event):
        self.widget1.pack_forget()
        LoginApplication.__init__(LoginApplication)

    def register(self, event):
        self.widget1.pack_forget()
        RegisterApplication.__init__(RegisterApplication)


def main():
    root = Tk()
    root.geometry("400x500")
    MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
           