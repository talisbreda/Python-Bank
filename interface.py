from tkinter import *
from tkinter import messagebox

from main import *

class MainApplication:
    def __init__(self, master=None):
        self.mainBody = Frame(master)
        self.mainBody.pack()

        self.title = Label(self.mainBody, bg='LightBlue', text="Bem-vindo ao banco Python!")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.registerTextContainer = Frame(self.mainBody, bg='lightgreen')
        self.registerTextContainer["width"] = 100
        self.registerTextContainer["height"] = 15
        self.registerTextContainer.pack(pady=(120, 0))

        self.registerText = Label(self.registerTextContainer, text="Registre-se")
        self.registerText["font"] = ("Verdana", "10", "bold")
        self.registerText.pack(side=LEFT, pady = (0, 5))

        self.registerButton = Button(self.mainBody, text="Registrar")
        self.registerButton["width"] = 15
        self.registerButton.bind("<Button-1>", self.registerModule)
        self.registerButton.pack(pady = 15)

        self.loginTextContainer = Frame(self.mainBody, bg='lightgreen')
        self.loginTextContainer["width"] = 100
        self.loginTextContainer["height"] = 15
        self.loginTextContainer.pack()

        self.loginText = Label(self.loginTextContainer, text="Login")
        self.loginText["font"] = ("Verdana", "10", "bold")
        self.loginText.pack(side=LEFT, pady = (0, 5))

        self.loginButton = Button(self.mainBody, text="Login")
        self.loginButton["width"] = 15
        self.loginButton.bind("<Button-1>", self.login)
        self.loginButton.pack(pady = 15)
















    
    def loginModule(self, event, master=None):
        self.mainBody.pack_forget()
        self.loginBody = Frame(master)
        self.loginBody.pack()

        self.title = Label(self.loginBody, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.loginBody, bg="white", text="Login")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 80)

        self.emailTextContainer = Frame(self.loginBody, bg='lightgreen')
        self.emailTextContainer["width"] = 100
        self.emailTextContainer["height"] = 15
        self.emailTextContainer.pack()

        self.emailText = Label(self.emailTextContainer, text="E-mail")
        self.emailText["font"] = ("Verdana", "10", "bold")
        self.emailText.pack(side=LEFT, pady = (0, 5))

        self.emailEntry = Entry(self.loginBody)
        self.emailEntry["width"] = 40
        self.emailEntry.pack()

        self.passwordTextContainer = Frame(self.loginBody, bg='lightgreen')
        self.passwordTextContainer["width"] = 40
        self.passwordTextContainer["height"] = 15
        self.passwordTextContainer.pack(pady = (30, 0))

        self.passwordText = Label(self.passwordTextContainer, text="Password")
        self.passwordText["font"] = ("Verdana", "10", "bold")
        self.passwordText["width"] = 10
        self.passwordText.pack(side = BOTTOM, padx = 5, pady = (0, 5))

        self.passwordEntry = Entry(self.loginBody, show='*')
        self.passwordEntry["width"] = 40
        self.passwordEntry.pack()

        self.loginButton = Button(self.loginBody, text="Login")
        self.loginButton["width"] = 15
        self.loginButton.pack(pady = 30)
        self.loginButton.bind("<Button-1>", self.login(self.emailEntry, self.passwordEntry))

        self.registerLink = Label(self.loginBody, text="Faça login", fg="blue", cursor="hand2")
        self.registerLink.bind("<Button-1>", self.redirectToRegister)
        self.registerLink.pack()
    
    def login(self, event, emailEntry, passwordEntry):
        email = emailEntry.get()
        password = passwordEntry.get()
        try:
            authenticate(email, password)
            self.bankModule
        except Exception as e:
            messagebox.showwarning("Error", e)

    def redirectToRegister(self, event):
        self.loginBody.pack_forget()
        self.registerModule()











   
    
        
    def registerModule(self, event, master=None):
        self.mainBody.pack_forget()
        self.registerBody = Frame(master)
        self.registerBody.pack()

        self.title = Label(self.registerBody, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.registerBody, bg="white", text="Register")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.nameTextContainer = Frame(self.registerBody)
        self.nameTextContainer["width"] = 100
        self.nameTextContainer["height"] = 15
        self.nameTextContainer.pack()

        self.nameText = Label(self.nameTextContainer, text="Insert your full name")
        self.nameText["font"] = ("Verdana", "10", "bold")
        self.nameText.pack(side=LEFT, pady = (0, 5))

        self.nameEntry = Entry(self.registerBody)
        self.nameEntry["width"] = 40
        self.nameEntry.pack()

        self.emailTextContainer = Frame(self.registerBody)
        self.emailTextContainer["width"] = 100
        self.emailTextContainer["height"] = 15
        self.emailTextContainer.pack(pady=(20, 0))

        self.emailText = Label(self.emailTextContainer, text="Insira seu e-mail")
        self.emailText["font"] = ("Verdana", "10", "bold")
        self.emailText.pack(side=LEFT, pady = (0, 5))

        self.emailEntry = Entry(self.registerBody)
        self.emailEntry["width"] = 40
        self.emailEntry.pack()

        self.phoneTextContainer = Frame(self.registerBody)
        self.phoneTextContainer["width"] = 100
        self.phoneTextContainer["height"] = 15
        self.phoneTextContainer.pack(pady=(20, 0))

        self.phoneText = Label(self.phoneTextContainer, text="Insira seu número de telefone")
        self.phoneText["font"] = ("Verdana", "10", "bold")
        self.phoneText.pack(side=LEFT, pady = (0, 5))

        self.phoneEntry = Entry(self.registerBody)
        self.phoneEntry["width"] = 40
        self.phoneEntry.pack()

        self.cpfTextContainer = Frame(self.registerBody)
        self.cpfTextContainer["width"] = 100
        self.cpfTextContainer["height"] = 15
        self.cpfTextContainer.pack(pady=(20, 0))

        self.cpfText = Label(self.cpfTextContainer, text="Insira seu RG")
        self.cpfText["font"] = ("Verdana", "10", "bold")
        self.cpfText.pack(side=LEFT, pady = (0, 5))

        self.cpfEntry = Entry(self.registerBody)
        self.cpfEntry["width"] = 40
        self.cpfEntry.pack()
        
        self.rgTextContainer = Frame(self.registerBody)
        self.rgTextContainer["width"] = 100
        self.rgTextContainer["height"] = 15
        self.rgTextContainer.pack(pady=(20, 0))

        self.rgText = Label(self.rgTextContainer, text="Insira seu CPF")
        self.rgText["font"] = ("Verdana", "10", "bold")
        self.rgText.pack(side=LEFT, pady = (0, 5))

        self.rgEntry = Entry(self.registerBody)
        self.rgEntry["width"] = 40
        self.rgEntry.pack()

        self.passwordTextContainer = Frame(self.registerBody)
        self.passwordTextContainer["width"] = 40
        self.passwordTextContainer["height"] = 15
        self.passwordTextContainer.pack(pady = (20, 0))

        self.passwordText = Label(self.passwordTextContainer, text="Insira uma senha")
        self.passwordText["font"] = ("Verdana", "10", "bold")
        self.passwordText.pack(side = BOTTOM, padx = 5, pady = (0, 5))

        self.passwordEntry = Entry(self.registerBody, show='*')
        self.passwordEntry["width"] = 40
        self.passwordEntry.pack()
        
        self.confirmPasswordTextContainer = Frame(self.registerBody)
        self.confirmPasswordTextContainer["width"] = 40
        self.confirmPasswordTextContainer["height"] = 15
        self.confirmPasswordTextContainer.pack(pady = (20, 0))

        self.confirmPasswordText = Label(self.confirmPasswordTextContainer, text="Confirme a senha")
        self.confirmPasswordText["font"] = ("Verdana", "10", "bold")
        self.confirmPasswordText.pack(side = BOTTOM, padx = 5, pady = (0, 5))

        self.confirmPasswordEntry = Entry(self.registerBody, show='*')
        self.confirmPasswordEntry["width"] = 40
        self.confirmPasswordEntry.pack()


        self.registerButton = Button(self.registerBody, text="Register")
        self.registerButton["width"] = 15
        self.registerButton.bind("<Button-1>", self.registerClient)
        self.registerButton.pack(pady = 20)


        self.loginLink = Label(self.registerBody, text="Faça login", fg="blue", cursor="hand2")
        self.loginLink.bind("<Button-1>", self.redirectToLogin)
        self.loginLink.pack()
    
    def registerClient(self, event):
        self.name = self.nameEntry.get()
        self.email = self.emailEntry.get()
        self.phone = self.phoneEntry.get()
        self.cpf = self.cpfEntry.get()
        self.rg = self.rgEntry.get()
        self.password = self.passwordEntry.get()

        try:
            createNewClient(self.name, self.email, self.phone, self.cpf, self.rg, self.password)
            self.registerBody.pack
            self.bankModule
        except Exception as e:
            messagebox.showwarning("Error", e)

    def redirectToLogin(self, event):
        self.registerBody.pack_forget()
        self.loginModule












    
    def bankModule(self, event, holder, master=None):
        self.bankBody = Frame(master)
        self.bankBody.pack()

        self.title = Label(self.bankBody, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.bankBody, bg="white", text="Choose the operation")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.depositButton = Button(self.bankBody, text="Deposit")
        self.depositButton["width"] = 15
        self.depositButton.bind("<Button-1>", self.deposit(self, holder))
        self.depositButton.pack(pady = 20)

        self.withdrawButton = Button(self.bankBody, text="Withdraw")
        self.withdrawButton["width"] = 15
        self.withdrawButton.bind("<Button-1>", self.withdraw(self, holder))
        self.withdrawButton.pack(pady = 20)

        self.transferButton = Button(self.bankBody, text="Transfer")
        self.transferButton["width"] = 15
        self.transferButton.bind("<Button-1>", self.transfer(self, holder))
        self.transferButton.pack(pady = 20)

    def deposit(self, event, holder, master=None):
        # Account.deposit
        self.bankBody.pack_forget()

        self.depositBody = Frame(master)
        self.depositBody.pack()

        self.title = Label(self.depositBody, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.depositBody, bg="white", text="Choose the value of the deposit")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.depositValueEntry = Entry(self.depositBody)
        self.depositValueEntry["width"] = 40
        self.depositValueEntry.pack()

        self.depositButton = Button(self.depositBody, text="Deposit")
        self.depositButton["width"] = 15
        self.depositButton.bind("<Button-1>", holder.dbUpdate(holder, 'deposit', self.depositValueEntry.get()))
        self.depositButton.pack(pady = 20)
    
    def withdraw(self, holder, master=None):
        self.bankBody.pack_forget()

        self.withdrawBody = Frame(master)
        self.withdrawBody.pack()

        self.title = Label(self.withdrawBody, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.withdrawBody, bg="white", text="Choose the value of the withdrawal")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.withdrawValueEntry = Entry(self.withdrawBody)
        self.withdrawValueEntry["width"] = 40
        self.withdrawValueEntry.pack()

        self.withdrawButton = Button(self.withdrawBody, text="withdraw")
        self.withdrawButton["width"] = 15
        self.withdrawButton.bind("<Button-1>", holder.dbUpdate(holder, 'withdraw', self.withdrawValueEntry.get()))
        self.withdrawButton.pack(pady = 20)
    
    def transfer(self, holder, master=None):
        self.bankBody.pack_forget()

        self.transferBody = Frame(master)
        self.transferBody.pack()

        self.title = Label(self.transferBody, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.transferBody, bg="white", text="Choose the value of the transfer")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.transferValueEntry = Entry(self.transferBody)
        self.transferValueEntry["width"] = 40
        self.transferValueEntry.pack()

        self.transferButton = Button(self.transferBody, text="transfer")
        self.transferButton["width"] = 15
        self.transferButton.bind("<Button-1>", holder.dbUpdate(holder, 'transfer', self.transferValueEntry.get()))
        self.transferButton.pack(pady = 20)

        self.backButton = Button(self.transferBody, text="Back to main page")
        self.backButton["width"] = 15
        self.backButton.bind("<Button-1>", self.__init__(self))
        self.backButton.pack(pady = 20)
    


def main():
    root = Tk()
    root.geometry("400x700")
    MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
           