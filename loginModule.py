from tkinter import *
from tkinter import messagebox

from main import authenticate

class LoginApplication:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.title = Label(self.widget1, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.widget1, bg="white", text="Login")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 80)

        self.emailTextContainer = Frame(self.widget1, bg='lightgreen')
        self.emailTextContainer["width"] = 100
        self.emailTextContainer["height"] = 15
        self.emailTextContainer.pack()

        self.emailText = Label(self.emailTextContainer, text="E-mail")
        self.emailText["font"] = ("Verdana", "10", "bold")
        self.emailText.pack(side=LEFT, pady = (0, 5))

        self.emailEntry = Entry(self.widget1)
        self.emailEntry["width"] = 40
        self.emailEntry.pack()

        self.passwordTextContainer = Frame(self.widget1, bg='lightgreen')
        self.passwordTextContainer["width"] = 40
        self.passwordTextContainer["height"] = 15
        self.passwordTextContainer.pack(pady = (30, 0))

        self.passwordText = Label(self.passwordTextContainer, text="Password")
        self.passwordText["font"] = ("Verdana", "10", "bold")
        self.passwordText["width"] = 10
        self.passwordText.pack(side = BOTTOM, padx = 5, pady = (0, 5))

        self.passwordEntry = Entry(self.widget1, show='*')
        self.passwordEntry["width"] = 40
        self.passwordEntry.pack()

        self.loginButton = Button(self.widget1, text="Login")
        self.loginButton["width"] = 15
        self.loginButton.bind("<Button-1>", self.login)
        self.loginButton.pack(pady = 30)
    
    def login(self, event):
        self.email = self.emailEntry.get()
        self.password = self.passwordEntry.get()
        try:
            authenticate(self.email, self.password)
        except:
            messagebox.showwarning("Error", "Credentials are incorrect")


root = Tk()
root.geometry("400x500")
LoginApplication(root)
root.mainloop()