from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+mysqlconnector://root:256984@localhost:3306/trabalho", echo=True, future=True)

class Account():


    def __init__(self, client, id) -> None:
        self.id = id
        self.client = client
        self.balance = 0
    
    def deposit(self):
        print("Insert the value of the deposit")
        value = float(input())
        self.balance = self.dbUpdate('deposit', int(value*100))
        print("New balance: $%.2f" % (self.balance/100))
    
    def withdraw(self):
        print("Insert the value of the withdrawal")
        value = float(input())
        self.balance = self.dbUpdate('withdraw', int(value*100))
    
    def transfer(self):
        print("Insert the value of the transfer")
        value = float(input())
        self.balance = self.dbUpdate('transfer', int(value*100))
        
    # def checkBalance(self, value):
    #     if value > self.balance: 
    #         print("Insufficient balance")
    #         print("Current balance: $%.2f" % (self.balance))
    #     else: 
    #         self.balance -= value
    #         print("New balance: $%.2f" % (self.balance))
            
    def dbUpdate(self, transaction, value):
        with engine.connect() as conn:
            result = conn.execute(
                text("SELECT balance FROM account WHERE idAccount = :id"),
                [{"id": int(self.id)}]
            )
            conn.commit()
        balance = int(result.scalar())
        if transaction == 'deposit':
            balance += value
        if transaction == 'withdraw':
            if value > balance:
                print("Insufficient balance")
            else:
                balance -= value
        if transaction == 'transfer':
            if value > balance:
                print("Insufficient balance")
            else:
                balance -= value
            # TODO
        with engine.connect() as conn:
            conn.execute(
                text("UPDATE account SET balance = :balance WHERE idAccount = :id"),
                [{"balance": balance, "id": self.id}]
            )
            conn.commit()
        return balance