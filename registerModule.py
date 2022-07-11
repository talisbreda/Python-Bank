from tkinter import *
from main import createNewClient

class RegisterApplication:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.title = Label(self.widget1, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.widget1, bg="white", text="Register")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.nameTextContainer = Frame(self.widget1)
        self.nameTextContainer["width"] = 100
        self.nameTextContainer["height"] = 15
        self.nameTextContainer.pack()

        self.nameText = Label(self.nameTextContainer, text="Insert your full name")
        self.nameText["font"] = ("Verdana", "10", "bold")
        self.nameText.pack(side=LEFT, pady = (0, 5))

        self.nameEntry = Entry(self.widget1)
        self.nameEntry["width"] = 40
        self.nameEntry.pack()

        self.emailTextContainer = Frame(self.widget1)
        self.emailTextContainer["width"] = 100
        self.emailTextContainer["height"] = 15
        self.emailTextContainer.pack(pady=(20, 0))

        self.emailText = Label(self.emailTextContainer, text="Insira seu e-mail")
        self.emailText["font"] = ("Verdana", "10", "bold")
        self.emailText.pack(side=LEFT, pady = (0, 5))

        self.emailEntry = Entry(self.widget1)
        self.emailEntry["width"] = 40
        self.emailEntry.pack()

        self.phoneTextContainer = Frame(self.widget1)
        self.phoneTextContainer["width"] = 100
        self.phoneTextContainer["height"] = 15
        self.phoneTextContainer.pack(pady=(20, 0))

        self.phoneText = Label(self.phoneTextContainer, text="Insira seu número de telefone")
        self.phoneText["font"] = ("Verdana", "10", "bold")
        self.phoneText.pack(side=LEFT, pady = (0, 5))

        self.phoneEntry = Entry(self.widget1)
        self.phoneEntry["width"] = 40
        self.phoneEntry.pack()

        self.cpfTextContainer = Frame(self.widget1)
        self.cpfTextContainer["width"] = 100
        self.cpfTextContainer["height"] = 15
        self.cpfTextContainer.pack(pady=(20, 0))

        self.cpfText = Label(self.cpfTextContainer, text="Insira seu RG")
        self.cpfText["font"] = ("Verdana", "10", "bold")
        self.cpfText.pack(side=LEFT, pady = (0, 5))

        self.cpfEntry = Entry(self.widget1)
        self.cpfEntry["width"] = 40
        self.cpfEntry.pack()
        
        self.rgTextContainer = Frame(self.widget1)
        self.rgTextContainer["width"] = 100
        self.rgTextContainer["height"] = 15
        self.rgTextContainer.pack(pady=(20, 0))

        self.rgText = Label(self.rgTextContainer, text="Insira seu CPF")
        self.rgText["font"] = ("Verdana", "10", "bold")
        self.rgText.pack(side=LEFT, pady = (0, 5))

        self.rgEntry = Entry(self.widget1)
        self.rgEntry["width"] = 40
        self.rgEntry.pack()

        self.passwordTextContainer = Frame(self.widget1)
        self.passwordTextContainer["width"] = 40
        self.passwordTextContainer["height"] = 15
        self.passwordTextContainer.pack(pady = (20, 0))

        self.passwordText = Label(self.passwordTextContainer, text="Insira uma senha")
        self.passwordText["font"] = ("Verdana", "10", "bold")
        self.passwordText.pack(side = BOTTOM, padx = 5, pady = (0, 5))

        self.passwordEntry = Entry(self.widget1, show='*')
        self.passwordEntry["width"] = 40
        self.passwordEntry.pack()
        
        self.confirmPasswordTextContainer = Frame(self.widget1)
        self.confirmPasswordTextContainer["width"] = 40
        self.confirmPasswordTextContainer["height"] = 15
        self.confirmPasswordTextContainer.pack(pady = (20, 0))

        self.confirmPasswordText = Label(self.confirmPasswordTextContainer, text="Confirme a senha")
        self.confirmPasswordText["font"] = ("Verdana", "10", "bold")
        self.confirmPasswordText.pack(side = BOTTOM, padx = 5, pady = (0, 5))

        self.confirmPasswordEntry = Entry(self.widget1, show='*')
        self.confirmPasswordEntry["width"] = 40
        self.confirmPasswordEntry.pack()


        self.registerButton = Button(self.widget1, text="Register")
        self.registerButton["width"] = 15
        self.registerButton.bind("<Button-1>", self.createClient)
        self.registerButton.pack(pady = 20)

    def createClient(self, event):
        self.name = self.nameEntry.get()
        self.email = self.emailEntry.get()
        self.phone = self.phoneEntry.get()
        self.cpf = self.cpfEntry.get()
        self.rg = self.rgEntry.get()
        self.password = self.passwordEntry.get()

        createNewClient(self.name, self.email, self.phone, self.cpf, self.rg, self.password)



root = Tk()
root.geometry("500x700")
RegisterApplication(root)
root.mainloop()