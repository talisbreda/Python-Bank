from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+mysqlconnector://root:256984@localhost:3306/trabalho", echo=True, future=True)

class Account():

    def __init__(self, client, id) -> None:
        self.id = id
        self.client = client
        self.balance = 0
    
    def retrieveBalance(self, id):
        with engine.connect() as conn:
            result = conn.execute(
                text("SELECT balance FROM account WHERE idAccount = :id"),
                [{"id": self.id}]
            )
            conn.commit()
        
        return result.scalar()
    
    def updateBalance(self, balance):
        with engine.connect() as conn:
            result = conn.execute(
                text("UPDATE account SET balance = :balance WHERE idAccount = :id"),
                [{"balance": balance, "id": self.id}]
            )
            conn.commit()
    
    # Deposita um valor na conta
    def deposit(self, value):
        # Atualiza o saldo da conta no banco de dados

        balance = self.retrieveBalance(self.id)
        balance += value
        print("Novo saldo: $%.2f" % (balance/100))
        self.updateBalance(balance)
    
    # Retira um valor na conta
    def withdraw(self, value):
        # Atualiza o saldo da conta no banco de dados
        # self.balance = self.dbUpdate('withdraw', int(value*100))

        balance = self.retrieveBalance(self.id)

        if value > balance:
            raise Warning("Saldo insuficiente")
        else:
            balance -= value
            print("Novo saldo: $%.2f" % (balance/100))
        
        self.updateBalance(balance)
    
    # Transfere um valor para outra conta
    def transfer(self, accNumber, agency, value):

        balance = self.retrieveBalance(self.id)

        if value > balance:
            raise Warning("Saldo insuficiente")
        else:
            balance -= value
            print("Novo saldo: $%.2f" % (balance/100))

        self.updateBalance(balance)
        self.transferToReceiver(accNumber, agency, value, balance)
    
    # Função responsável por atualizar os dados da conta receptora de uma transferência
    def transferToReceiver(self, accNumber, agency, value, balance):
        
        try:
            with engine.connect() as conn:
                result = conn.execute(
                    text("SELECT balance FROM account WHERE accNumber = :accNumber and agency = :agency"),
                    [{"balance": balance, "accNumber": accNumber, "agency": agency}]
                )
            conn.commit()

            newBalance = int(result.scalar()) + value

            with engine.connect() as conn:
                conn.execute(
                    text("UPDATE account SET balance = :balance WHERE accNumber = :accNumber and agency = :agency"),
                    [{"balance": newBalance, "accNumber": accNumber, "agency": agency}]
                )
                conn.commit()
        except:
            # Caso o resultado seja nulo (a conta não existe), cria um erro a ser tratado 
            # na função dbUpdate
            raise Exception("Conta não existe")
        
    def testResult(self, result):
        if result is None:
            raise Exception("Credenciais estão incorretas")
        else:
            return result
    
    def getId(self):
        return self.id
        