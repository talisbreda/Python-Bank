# Imports de classe
from pickle import FALSE
from account import Account
from client import Client

# Imports de bibliotecas
from sqlalchemy import create_engine
from sqlalchemy import text
from random import randint
from hashlib import sha3_256
import re

# Criação da engine do SQLAlchemy para acesso global ao banco de dados
engine = create_engine("mysql+mysqlconnector://root:256984@localhost:3306/trabalho", echo=True, future=True)

# Cria um novo cliente no banco de dados com base em inputs do usuario
def createNewClient(name, email, phone, cpf, rg, password):
    id = randint(100000, 999999)

    # Criptografia da senha inserida pelo usuário, usando SHA256
    passcode = sha3_256(password.encode('UTF-8')).hexdigest()

    # Verifica a unicidade do ID gerado
    id = checkId(id, "client")
    # Verifica se o email inserido é válido ou se já está registrado
    checkEmail(email)
    valid = checkCPF(cpf)
    
    if valid:
    # Cria uma conexão para inserir uma nova linha na tabela de clientes do banco de dados
        with engine.connect() as conn:
            conn.execute(
                text("INSERT INTO client (idClient, passcode, fullname, email, phone, cpf, rg) VALUES (:id, :passcode, :fullname, :email, :phone, :cpf, :rg)"),
                [{"id": id, "passcode": passcode, "fullname": name, "email": email, "phone": phone, "cpf": cpf, "rg": rg}]
            )
            conn.commit()
        # Instancia uma classe com os dados do cliente
        client = Client(id, name, email, phone, cpf, rg, True)
        # Acessa os serviços bancários na conta recém registrada
        return bank(client)
    else:
        raise Exception("CPF é inválido")

# Checa a validade do e-mail e a sua existência no banco de dados
def checkEmail(email):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT email FROM client WHERE email = :email"),
            [{"email": email}]
        )
        conn.commit()
    # Validação do e-mail, tanto relacionada à sintaxe quanto à unicidade
    if re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email) is None: 
        raise Exception("E-mail inválido")
    if result.scalar() is not None: 
        raise Exception("E-mail já está em uso")

def checkCPF(cpf):

    count = 2
    def checkDigit(digit):
        sum = 0
        for i in range (n-count):
            sum += int(str(cpf)[i]) * ((n-count+1)-i)
        if sum % 11 < 2 and int(digit) == 0:
            return True
        elif sum % 11 >= 2 and int(digit) == 11 - sum % 11:
            return True
        else:
            return False

    n = len(str(cpf))
    if n != 11:
        return False
    if cpf == cpf[::-1]:
        return False
    valid = checkDigit(str(cpf)[9])
    count = 1
    if valid: valid = checkDigit(str(cpf)[10])

    if valid: return True
    else: return False
    

# Cria uma nova conta no banco de dados
def createNewAccount(holder):

    # Geração de um ID e de um número de conta
    id = checkId(randint(100000, 999999), "account")
    accNum = checkAcc(randint(100000, 999999))

    # Conexão para inserção de uma nova linha na tabela de contas do banco de dados
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO account (idAccount, holder, accNumber, agency, accType, balance) VALUES (:id, :holder, :accNumber, :agency, :accType, :balance)"),
            [{"id": id, "holder": holder.getId(), "accNumber": accNum, "agency": 1, "accType": 1, "balance": 0}]
        )
        conn.commit()
    # Retorna uma classe instanciada de Account
    return Account(holder, id)

# Testa se o retorno do banco de dados é nulo, e retorna um erro caso for
def testResult(result):
    if result is None:
        raise Exception("Credenciais estão incorretas")
    else:
        return result

# Realiza a autenticação de um usuário    
def authenticate(email, password):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT passcode FROM client WHERE email = :email"),
            [{"email": email}]
        )
        conn.commit()

    # Testa o resultado da busca no banco de dados, e retorna um erro caso esta seja nula
    passcode = testResult(result.scalar())
    # Criptografa a senha inserida e compara com a já existente no banco de dados
    encPassword = sha3_256(password.encode('UTF-8')).hexdigest()
    if encPassword == passcode:
        return accessClient(email)
    else:
        # Gera um erro caso algo as senhas sejam diferentes
        raise Exception("Credenciais estão incorretas")


# Confere a unicidade do ID gerado
def checkId(id, table):
    with engine.connect() as conn:
        # Confere o ID de diferentes tabelas de acordo com o tipo de ID gerado
        if table == "account":
            result = conn.execute(
                text("SELECT idAccount FROM account WHERE idAccount = :id"),
                [{"id": id}]
            )
        else:
            result = conn.execute(
                text("SELECT idClient FROM client WHERE idClient = :id"),
                [{"id": id}]
            )
        conn.commit()
    # Testa o resultado da busca para saber se é nulo
    try:
        # testResult retorna um erro caso o parâmetro seja nulo, o que significa que o
        # ID não existe no banco de dados e a inserção pode continuar
        test = testResult(result.scalar())
        # result.scalar() retorna o primeiro elemento da primeira linha da chamada
        newid = randint(100000, 999999)
        checkId(newid, table)
    except:
        return id
    
# Checa a unicidade do número da conta gerado
def checkAcc(accNum):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT accNumber FROM account WHERE accNumber = :accNumber"),
            [{"accNumber": accNum}]
        )
        conn.commit()
    try:
        test = testResult(result.scalar())
        newAccNum = checkAcc(randint(100000, 999999))
        return newAccNum
    except:
        return accNum

# Após autenticação, é instanciada uma classe Client com as informações necessárias trazidas do banco 
# de dados, para que se possa efetuar as operações necessárias
def accessClient(email):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT idClient, fullname, phone, cpf, rg FROM client WHERE email = :email"),
            [{"email": email}])
        conn.commit()
    # result.first() retorna a primeira linha da chamada, que corresponde aos dados do cliente
    result = result.first()
    # Instanciação da classe Client
    client = Client(result[0], result[1], email, result[2], result[3], result[4], False)
    # Acesso aos serviços bancários a partir da conta do cliente
    return bank(client)

# Instanciação da classe Account para realização dos serviços
def accessAccount(holder):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT idAccount, accNumber, agency, accType, balance FROM account WHERE holder = :holder"),
            [{"holder": holder.getId()}])
        conn.commit()
    id = result.scalar()
    return Account(holder, id)

def bank(client):
    # Se o cliente foi recém-criado, é necessário criar uma nova linha na tabela de contas do
    # banco de dados
    if client.getNew() == False:
        return accessAccount(client)
    else:
        client.setNew(False)
        return createNewAccount(client)
            