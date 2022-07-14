from email import message
from tkinter import *
from tkinter import messagebox

from main import *

class MainApplication:
    def __init__(self, master=None):
        self.mainBody = Frame(master)
        self.mainBody.pack()

        self.title = Label(self.mainBody, text="Bem-vindo ao banco Python!")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.registerTextContainer = Frame(self.mainBody)
        self.registerTextContainer["width"] = 100
        self.registerTextContainer["height"] = 15
        self.registerTextContainer.pack(pady=(120, 0))

        self.registerText = Label(self.registerTextContainer, text="Registre-se")
        self.registerText["font"] = ("Verdana", "10", "bold")
        self.registerText.pack(side=LEFT, pady = (0, 5))

        self.registerButton = Button(self.mainBody, text="Registrar")
        self.registerButton["width"] = 15
        self.registerButton.bind("<ButtonRelease>", self.registerModule)
        self.registerButton.pack(pady = 15)

        self.loginTextContainer = Frame(self.mainBody)
        self.loginTextContainer["width"] = 100
        self.loginTextContainer["height"] = 15
        self.loginTextContainer.pack()

        self.loginText = Label(self.loginTextContainer, text="Login")
        self.loginText["font"] = ("Verdana", "10", "bold")
        self.loginText.pack(side=LEFT, pady = (0, 5))

        self.loginButton = Button(self.mainBody, text="Login")
        self.loginButton["width"] = 15
        self.loginButton.bind("<ButtonRelease>", self.loginModule)
        self.loginButton.pack(pady = 15)
















    
    def loginModule(self, event, master=None):
        self.mainBody.pack_forget()
        self.loginBody = Frame(master)
        self.loginBody.pack()

        self.title = Label(self.loginBody, text="Banco Python")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.loginBody, text="Login")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 80)

        self.emailTextContainer = Frame(self.loginBody)
        self.emailTextContainer["width"] = 100
        self.emailTextContainer["height"] = 15
        self.emailTextContainer.pack()

        self.emailText = Label(self.emailTextContainer, text="E-mail")
        self.emailText["font"] = ("Verdana", "10", "bold")
        self.emailText.pack(side=LEFT, pady = (0, 5))

        self.emailEntry = Entry(self.loginBody)
        self.emailEntry["width"] = 40
        self.emailEntry.pack()

        self.passwordTextContainer = Frame(self.loginBody)
        self.passwordTextContainer["width"] = 40
        self.passwordTextContainer["height"] = 15
        self.passwordTextContainer.pack(pady = (30, 0))

        self.passwordText = Label(self.passwordTextContainer, text="Senha")
        self.passwordText["font"] = ("Verdana", "10", "bold")
        self.passwordText["width"] = 10
        self.passwordText.pack(side = BOTTOM, padx = 5, pady = (0, 5))

        self.passwordEntry = Entry(self.loginBody, show='*')
        self.passwordEntry["width"] = 40
        self.passwordEntry.pack()

        self.loginButton = Button(self.loginBody, text="Login")
        self.loginButton["width"] = 15
        self.loginButton.pack(pady = 30)

        self.registerLink = Label(self.loginBody, text="Não tem conta? Registre-se", fg="blue", cursor="hand2")
        self.registerLink.bind("<ButtonRelease>", self.redirectToRegister)
        self.registerLink.pack()
    
        self.loginButton.bind("<ButtonRelease>", self.login)
        
    def login(self, event):
        self.email = self.emailEntry.get()
        self.password = self.passwordEntry.get()
        # email = emailEntry.get()
        # password = passwordEntry.get()
        try:
            account = authenticate(self.email, self.password)
            self.loginBody.pack_forget()
            self.bankModule(self, account)
        except Exception as e:
            messagebox.showwarning("Erro", e)

    def redirectToRegister(self, event):
        self.loginBody.pack_forget()
        self.registerModule(self)











   
    
        
    def registerModule(self, event, master=None):
        self.mainBody.pack_forget()
        self.registerBody = Frame(master)
        self.registerBody.pack()

        self.title = Label(self.registerBody, text="Banco Python")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.registerBody, text="Registrar-se")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.nameTextContainer = Frame(self.registerBody)
        self.nameTextContainer["width"] = 100
        self.nameTextContainer["height"] = 15
        self.nameTextContainer.pack()

        self.nameText = Label(self.nameTextContainer, text="Insira seu nome completo")
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


        self.registerButton = Button(self.registerBody, text="Registrar")
        self.registerButton["width"] = 15
        self.registerButton.bind("<ButtonRelease>", self.registerClient)
        self.registerButton.pack(pady = 20)


        self.loginLink = Label(self.registerBody, text="Já tem uma conta? Faça login", fg="blue", cursor="hand2")
        self.loginLink.bind("<ButtonRelease>", self.redirectToLogin)
        self.loginLink.pack()
    
    def registerClient(self, event):
        self.name = self.nameEntry.get()
        self.email = self.emailEntry.get()
        self.phone = self.phoneEntry.get()
        self.cpf = self.cpfEntry.get()
        self.rg = self.rgEntry.get()
        self.password = self.passwordEntry.get()
        self.confirmPassword = self.confirmPasswordEntry.get()

        valid = True

        try:
            if self.name=="" or self.email=="" or self.phone=="" or self.cpf=="" or self.rg=="" or self.password=="" or self.confirmPassword=="":
                messagebox.showwarning("Erro", "Por favor preencha todos os campos")
            else:
                phone = int(self.phone)
                cpf = int(self.cpf)
                rg = int(self.rg)

                if self.password == self.confirmPassword:
                    try:
                        acc = createNewClient(self.name, self.email, self.phone, self.cpf, self.rg, self.password)
                        self.registerBody.pack_forget()
                        self.bankModule(self, acc)
                    except Exception as e:
                        messagebox.showwarning("Erro", e)
                else:
                    messagebox.showwarning("Erro", "As senhas não correspondem")
        except ValueError:
            messagebox.showwarning("Erro", "Os campos telefone, CPF e RG devem conter APENAS números")

    def redirectToLogin(self, event):
        self.registerBody.pack_forget()
        self.loginModule(self)












    
    def bankModule(self, event, account, master=None):
        def preDeposit(event):
            self.depositModule(self, account)
        
        def preWithdraw(event):
            self.withdrawModule(self, account)

        def preTransfer(event):
            self.transferModule(self, account)

        def backToHome(event):
            res = messagebox.askquestion('Sair', 'Tem certeza que deseja sair?')
            if res == 'yes':
                self.bankBody.pack_forget() 
                self.__init__()
            elif res == 'no':
                return False

        self.bankBody = Frame(master)
        self.bankBody.pack()

        self.title = Label(self.bankBody, text="Banco Python")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.bankBody, text="Escolha a operação a realizar")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        text = "Saldo: R$: {balance}".format(balance = str((account.retrieveBalance(account.getId()))/100))
        self.balance = Label(self.bankBody, text=text)
        self.balance["font"] = ("Verdana", "12", "bold")
        self.balance.pack(pady = 10)

        self.depositButton = Button(self.bankBody, text="Depositar")
        self.depositButton["width"] = 15
        self.depositButton.pack(pady = 20)
        self.depositButton.bind("<ButtonRelease>", preDeposit)

        self.withdrawButton = Button(self.bankBody, text="Sacar")
        self.withdrawButton["width"] = 15
        self.withdrawButton.bind("<ButtonRelease>", preWithdraw)
        self.withdrawButton.pack(pady = 20)

        self.transferButton = Button(self.bankBody, text="Transferir")
        self.transferButton["width"] = 15
        self.transferButton.bind("<ButtonRelease>", preTransfer)
        self.transferButton.pack(pady = 20)

        self.backToHomeButton = Button(self.bankBody, text="Sair")
        self.backToHomeButton["width"] = 15
        self.backToHomeButton.pack(side=LEFT, pady=10)
        self.backToHomeButton.bind("<ButtonRelease>", backToHome)


    def depositModule(self, event, account, master=None):
        def update(event):
            account.deposit(int(float(self.depositValueEntry.get())*100))
            self.depositBody.pack_forget()
            self.showBalance(self, account)

        def backToMain(event):
            self.depositBody.pack_forget()
            self.bankModule(self, account)

        self.bankBody.pack_forget()

        self.depositBody = Frame(master)
        self.depositBody.pack()

        self.title = Label(self.depositBody, text="Banco Python")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.depositBody, text="Escolha o valor do depósito")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.depositValueEntry = Entry(self.depositBody)
        self.depositValueEntry["width"] = 40
        self.depositValueEntry.pack()

        self.confirmDepositButton = Button(self.depositBody, text="Depositar")
        self.confirmDepositButton["width"] = 15
        self.confirmDepositButton.bind("<ButtonRelease>", update)
        self.confirmDepositButton.pack(pady = 20)

        self.backToMainButton = Button(self.depositBody, text="Voltar")
        self.backToMainButton["width"] = 15
        self.backToMainButton.pack(side=LEFT, pady=10)
        self.backToMainButton.bind("<ButtonRelease>", backToMain)

    
    def withdrawModule(self, event, account, master=None):
        def update(event):
            try:
                account.withdraw(int(float(self.withdrawValueEntry.get())*100))
                self.withdrawBody.pack_forget()
                self.showBalance(self, account)
            except Exception as e:
                messagebox.showwarning("Erro", e)
        def backToMain(event):
            self.withdrawBody.pack_forget()
            self.bankModule(self, account)

        self.bankBody.pack_forget()

        self.withdrawBody = Frame(master)
        self.withdrawBody.pack()

        self.title = Label(self.withdrawBody, text="Banco Python")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.withdrawBody, text="Escolha o valor do saque")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.withdrawValueEntry = Entry(self.withdrawBody)
        self.withdrawValueEntry["width"] = 40
        self.withdrawValueEntry.pack()

        self.confirmWithdrawButton = Button(self.withdrawBody, text="Sacar")
        self.confirmWithdrawButton["width"] = 15
        self.confirmWithdrawButton.bind("<ButtonRelease>", update)
        self.confirmWithdrawButton.pack(pady = 20)

        self.backToMainButton = Button(self.withdrawBody, text="Voltar")
        self.backToMainButton["width"] = 15
        self.backToMainButton.pack(side=LEFT, pady=10)
        self.backToMainButton.bind("<ButtonRelease>", backToMain)

    
    def transferModule(self, event, account, master=None):
        def update(event):
            try:
                accNumber = int(self.accNumEntry.get())
                agency = int(self.agencyEntry.get())
                value = int(float(self.transferValueEntry.get())*100)

                account.transfer(accNumber, agency, value)
                self.transferBody.pack_forget()
                self.showBalance(self, account)
            except Exception as e:
                messagebox.showwarning("Erro", e)
        def backToMain(event):
            self.transferBody.pack_forget()
            self.bankModule(self, account)

        self.bankBody.pack_forget()

        self.transferBody = Frame(master)
        self.transferBody.pack()

        self.title = Label(self.transferBody, text="Banco Python")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.transferBody, text="Insira os dados da conta do receptor")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = (55, 20))

        self.accNumText = Label(self.transferBody, text="Número da conta")
        self.accNumText["font"] = ("Verdana", "10", "bold")
        self.accNumText.pack(pady = (0, 5))

        self.accNumEntry = Entry(self.transferBody)
        self.accNumEntry["width"] = 40
        self.accNumEntry.pack()

        self.agencyText = Label(self.transferBody, text="Agência")
        self.agencyText["font"] = ("Verdana", "10", "bold")
        self.agencyText.pack(pady = (0, 5))

        self.agencyEntry = Entry(self.transferBody)
        self.agencyEntry["width"] = 40
        self.agencyEntry.pack()

        self.subtitle = Label(self.transferBody, text="Insira o valor da transferência")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = (30, 20))

        self.transferValueEntry = Entry(self.transferBody)
        self.transferValueEntry["width"] = 40
        self.transferValueEntry.pack()

        self.confirmTransferButton = Button(self.transferBody, text="Transferir")
        self.confirmTransferButton["width"] = 15
        self.confirmTransferButton.bind("<ButtonRelease>", update)
        self.confirmTransferButton.pack(pady = 20)

        self.backToMainButton = Button(self.transferBody, text="Voltar")
        self.backToMainButton["width"] = 15
        self.backToMainButton.pack(side=LEFT, pady=10)  
        self.backToMainButton.bind("<ButtonRelease>", backToMain)
    
    def showBalance(self, event, account, master=None):
        def backToMain(event):
            self.balanceBody.pack_forget()
            self.bankModule(self, account)

        self.balanceBody = Frame(master)
        self.balanceBody.pack()

        self.title = Label(self.balanceBody, text="Banco Python")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.balanceBody, text="Novo saldo:")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = (55, 0))

        text = "R$: {balance}".format(balance = str((account.retrieveBalance(account.getId()))/100))
        self.balance = Label(self.balanceBody, text=text)
        self.balance["font"] = ("Verdana", "16", "bold")
        self.balance.pack(pady=20)

        self.backToMainButton = Button(self.balanceBody, text="Voltar")
        self.backToMainButton["width"] = 15
        self.backToMainButton.pack(pady=10)  
        self.backToMainButton.bind("<ButtonRelease>", backToMain)


def main():
    root = Tk()
    root.geometry("400x700")
    MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
           