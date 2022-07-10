from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+mysqlconnector://root:256984@localhost:3306/trabalho", echo=True, future=True)

class Account():

    def __init__(self, client, id) -> None:
        self.id = id
        self.client = client
        self.balance = 0
    
    # Deposita um valor na conta
    def deposit(self):
        print("Insert the value of the deposit")
        value = float(input())
        # Atualiza o saldo da conta no banco de dados
        self.balance = self.dbUpdate('deposit', int(value*100))
    
    # Retira um valor na conta
    def withdraw(self):
        print("Insert the value of the withdrawal")
        value = float(input())
        # Atualiza o saldo da conta no banco de dados
        self.balance = self.dbUpdate('withdraw', int(value*100))
    
    # Transfere um valor para outra conta
    def transfer(self):
        print("Insert the value of the transfer")
        value = float(input())
        self.balance = self.dbUpdate('transfer', int(value*100))
    
    # Função responsável por fazer atualizações no banco de dados, recebendo o valor da alteração
    # e a operação a ser realizada
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
            print("New balance: $%.2f" % (balance/100))
        if transaction == 'withdraw':
            if value > balance:
                print("Insufficient balance")
            else:
                balance -= value
                print("New balance: $%.2f" % (balance/100))
        if transaction == 'transfer':
            if value > balance:
                print("Insufficient balance")
            else:
                print("Insert the receiver's account number")
                accNumber = int(input())
                print("Insert the receiver's agency")
                agency = int(input())
                try:
                    # Chama a função responsável por buscar a conta receptora no banco de dados e 
                    # atualizar seu saldo
                    self.transferToReceiver(accNumber, agency, value)
                    balance -= value
                    print("New balance: $%.2f" % (balance/100))
                except: 
                    print("Account not found")
        
        # Atualiza o saldo da conta instanciada
        with engine.connect() as conn:
            conn.execute(
                text("UPDATE account SET balance = :balance WHERE idAccount = :id"),
                [{"balance": balance, "id": self.id}]
            )
            conn.commit()
        return balance
    
    # Função responsável por atualizar os dados da conta receptora de uma transferência
    def transferToReceiver(self, accNumber, agency, value):
        with engine.connect() as conn:
            result = conn.execute(
                text("SELECT balance FROM account WHERE accNumber = :accNumber and agency = :agency"),
                [{"accNumber": accNumber, "agency": agency}]
            )
            conn.commit()
        try:
            # Se o resultado não for nulo, significa que a conta existe e a operação pode ser realizada
            balance = self.testResult(result.scalar())
            balance += value
            with engine.connect() as conn:
                conn.execute(
                    text("UPDATE account SET balance = :balance WHERE accNumber = :accNumber"),
                    [{"balance": balance, "accNumber": accNumber}]
                )
                conn.commit()
        except:
            # Caso o resultado seja nulo (a conta não existe), cria um erro a ser tratado 
            # na função dbUpdate
            raise Exception
        
    def testResult(self, result):
        if result is None:
            raise Exception("Credentials are incorrect")
        else:
            return result
        