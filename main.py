from account import Account
from client import Client
from sqlalchemy import create_engine
from sqlalchemy import text
from random import randint
from cryptography.fernet import Fernet
from hashlib import sha3_256

engine = create_engine("mysql+mysqlconnector://root:256984@localhost:3306/trabalho", echo=True, future=True)
key = Fernet.generate_key()
fernet = Fernet(key)

def createNewClient():
    id = randint(100000, 999999)
    print("Please insert your name")
    fullname = input()
    print("Please insert your e-mail")
    email = input()
    print("Please insert a phone number")
    phone = input()
    print("Please insert your CPF")
    cpf = input()
    print("Please insert your RG")
    rg = input()
    print("Please insert a password")
    passcode = sha3_256(input().encode('UTF-8')).hexdigest()

    checkId(id)
    valid = checkEmail(email)
    
    if valid:
        with engine.connect() as conn:
            conn.execute(
                text("INSERT INTO client (idClient, passcode, fullname, email, phone, cpf, rg) VALUES (:id, :passcode, :fullname, :email, :phone, :cpf, :rg)"),
                [{"id": id, "passcode": passcode, "fullname": fullname, "email": email, "phone": phone, "cpf": cpf, "rg": rg}]
            )
            conn.commit()
        client = Client(id, fullname, email, phone, cpf, rg, True)
        bank(client)
    else:
        createNewClient()

def createNewAccount(holder):

    id = checkId(randint(100000, 999999))
    accNum = checkAcc(randint(100000, 999999))
    
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO account (idAccount, holder, accNumber, agency, accType, balance) VALUES (:id, :holder, :accNumber, :agency, :accType, :balance)"),
            [{"id": id, "holder": holder.getId(), "accNumber": accNum, "agency": 1, "accType": 1, "balance": 0}]
        )
        conn.commit()
    return Account(holder, id)

def testResult(result):
    if result is None:
        raise Exception("Credentials are incorrect")
    else:
        return result
    
def authenticate(email, password):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT passcode FROM client WHERE email = :email"),
            [{"email": email}]
        )
        conn.commit()
    try:
        passcode = testResult(result.scalar())
        encPassword = sha3_256(password.encode('UTF-8')).hexdigest()
        if encPassword == passcode:
            accessClient(email)
        else:
            raise Exception("Credentials are incorrect")
    except Exception as e:
        print(e)


def checkId(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT idClient FROM client WHERE idClient = :id"),
            [{"id": id}]
        )
        conn.commit()
    try:
        test = testResult(result.one())
        newid = randint(100000, 999999)
        checkId(newid)
    except:
        return id

def checkEmail(email):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT email FROM client WHERE email = :email"),
            [{"email": email}]
        )
        conn.commit()
    try:
        test = testResult(result.one())
        print("E-mail is already in use")
        return False
    except:
        return True

    
def checkAcc(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT idAccount FROM account WHERE idAccount = :id"),
            [{"id": id}]
        )
        conn.commit()
    if result.scalar() != '':
        id = randint(100000, 999999)
        newid = checkId(id)
        return newid
    else:
        return id

def accessClient(email):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT idClient, fullname, phone, cpf, rg FROM client WHERE email = :email"),
            [{"email": email}])
        conn.commit()
    result = result.first()
    client = Client(result[0], result[1], email, result[2], result[3], result[4], False)
    bank(client)

def accessAccount(holder):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT idAccount, accNumber, agency, accType, balance FROM account WHERE holder = :holder"),
            [{"holder": holder.getId()}])
        conn.commit()
    id = result.scalar()
    return Account(holder, id)

def bank(client):
    if client.getNew() == False:
        acc = accessAccount(client)
    else:
        acc = createNewAccount(client)
        client.setNew(False)
    while True:

        print("Type 1 to deposit, 2 to withdraw, 3 to transfer, 4 to leave")
        try:
            n = int(input())

            match n:
                case 1:
                    acc.deposit()
                    continue
                case 2:
                    acc.withdraw()
                    continue
                case 3:
                    acc.transfer()
                    continue
                case 4:
                    break
        except ValueError: 
            print("Please insert a valid number")

while True:

    print("Type 1 to sign in, 2 to register, 3 to stop")
    try:
        m = int(input())

        match m:
            case 1:
                print("E-mail:")
                loginEmail = input()
                print("Password")
                loginPassword = input()
                authenticate(loginEmail, loginPassword)
            case 2:
                createNewClient()
                continue
            case 3:
                break
    except ValueError: 
            print("Please insert a valid number")


            