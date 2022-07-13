from tkinter import *
from tkinter import messagebox

from account import Account
           
class BankApplication:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.title = Label(self.widget1, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.widget1, bg="white", text="Choose the operation")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.depositButton = Button(self.widget1, text="Deposit")
        self.depositButton["width"] = 15
        self.depositButton.bind("<Button-1>", self.deposit(self, event=None))
        self.depositButton.pack(pady = 20)

        self.withdrawButton = Button(self.widget1, text="Withdraw")
        self.withdrawButton["width"] = 15
        self.withdrawButton.bind("<Button-1>", self.withdraw)
        self.withdrawButton.pack(pady = 20)

        self.transferButton = Button(self.widget1, text="Transfer")
        self.transferButton["width"] = 15
        self.transferButton.bind("<Button-1>", self.transfer)
        self.transferButton.pack(pady = 20)

    def deposit(self, event, master=None):
        # Account.deposit
        self.widget1.pack_forget()

        self.widget2 = Frame(master)
        self.widget2.pack()

        self.title = Label(self.widget2, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.widget2, bg="white", text="Choose the value of the deposit")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.depositValueEntry = Entry(self.widget2)
        self.depositValueEntry["width"] = 40
        self.depositValueEntry.pack()

        self.depositButton = Button(self.widget2, text="Deposit")
        self.depositButton["width"] = 15
        self.depositButton.bind("<Button-1>", Account.dbUpdate(Account, 'deposit', self.depositValueEntry.get()))
        self.depositButton.pack(pady = 20)
    
    def withdraw(self, master=None):
        self.widget1.pack_forget()

        self.widget3 = Frame(master)
        self.widget3.pack()

        self.title = Label(self.widget3, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.widget3, bg="white", text="Choose the value of the withdrawal")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.withdrawValueEntry = Entry(self.widget3)
        self.withdrawValueEntry["width"] = 40
        self.withdrawValueEntry.pack()

        self.withdrawButton = Button(self.widget3, text="withdraw")
        self.withdrawButton["width"] = 15
        self.withdrawButton.bind("<Button-1>", Account.dbUpdate(Account, 'withdraw', self.withdrawValueEntry.get()))
        self.withdrawButton.pack(pady = 20)
    
    def transfer(self, master=None):
        self.widget1.pack_forget()

        self.widget4 = Frame(master)
        self.widget4.pack()

        self.title = Label(self.widget4, bg='LightBlue', text="Bank")
        self.title["font"] = ("Verdana", "16", "bold")
        self.title.pack()

        self.subtitle = Label(self.widget4, bg="white", text="Choose the value of the transfer")
        self.subtitle["font"] = ("Verdana", "12", "bold")
        self.subtitle.pack(pady = 55)

        self.transferValueEntry = Entry(self.widget4)
        self.transferValueEntry["width"] = 40
        self.transferValueEntry.pack()

        self.transferButton = Button(self.widget4, text="transfer")
        self.transferButton["width"] = 15
        self.transferButton.bind("<Button-1>", Account.dbUpdate(Account, 'transfer', self.transferValueEntry.get()))
        self.transferButton.pack(pady = 20)

        self.backButton = Button(self.widget4, text="Back to main page")
        self.backButton["width"] = 15
        self.backButton.bind("<Button-1>", self.__init__(self))
        self.backButton.pack(pady = 20)
        

def main():
    root = Tk()
    root.geometry("500x700")
    BankApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()