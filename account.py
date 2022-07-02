class Account():


    def __init__(self, new) -> None:
        self.balance = 0
 

    def deposit(self):
        print("Insert the value of the deposit")
        value = float(input())
        self.balance += value
        print("New balance: $%.2f" % (self.balance))
    
    def withdraw(self):
        print("Insert the value of the withdrawal")
        value = float(input())
        self.checkBalance(value)
    
    def transfer(self):
        print("Insert the value of the transfer")
        value = float(input())
        self.checkBalance(value)
        
    def checkBalance(self, value):
        if value > self.balance: 
            print("Insufficient balance")
            print("Current balance: $%.2f" % (self.balance))
        else: 
            self.balance -= value
            print("New balance: $%.2f" % (self.balance))