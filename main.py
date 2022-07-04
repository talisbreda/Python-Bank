from account import Account
from client import Client
from sqlalchemy import create_engine
from sqlalchemy import text
from random import randint
from cryptography.fernet import Fernet

engine = create_engine("mysql+mysqlconnector://root:256984@localhost:3306/trabalho", echo=True, future=True)
key = Fernet.generate_key()
fernet = Fernet(key)

def createNewClient():

    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO client (idClient, passcode, fullname, email, phone, cpf, rg) VALUES (:id, :passcode, :fullname, :email, :phone, :cpf, :rg)"),
            [{"id": id, "passcode": passcode, "fullname": fullname, "email": email, "phone": phone, "cpf": cpf, "rg": rg}]
        )
        conn.commit()

def createNewAccount(holder):

    id = randint(000000, 999999)
    accNumber = randint(00000000, 99999999)
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO account (idAccount, holder, accNumber, agency, accType, balance) VALUES (:id, :holder, :accNumber, :agency, :accType, :balance)"),
            [{"id": id, "holder": holder.getId(), "accNumber": accNumber, "agency": 1, "accType": 1, "balance": 0}]
        )
        conn.commit()
    return Account(holder)

def authenticate(email, password):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT passcode FROM client WHERE email = :email"),
            [{"email": email}]
        )
        conn.commit()
    accessClient(email)
    # passcode = bytes(result.scalar(), 'UTF-8')
    # decPasscode = fernet.decrypt(passcode).decode()
    # if decPasscode == password:
    #     accessClient(email)

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
            text("SELECT accNumber, agency, accType, balance FROM account WHERE holder = :holder"),
            [{"holder": holder.getId()}])
        conn.commit()
    result = result.first()
    return Account(holder)

def bank(client):
    if client.getNew() == False:
        acc = accessAccount(client)
    else:
        acc = createNewAccount(client)
        client.setNew(False)
    while True:

        print("Type 1 to deposit, 2 to withdraw, 3 to transfer, 4 to leave")
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

while True:

    print("Type 1 to sign in, 2 to register, 3 to stop")
    m = int(input())

    match m:
        case 1:
            print("E-mail:")
            loginEmail = input()
            print("Password")
            loginPassword = input()
            authenticate(loginEmail, loginPassword)
        case 2:
            id = randint(000000, 999999)
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
            passcode = fernet.encrypt(input().encode())
            
            createNewClient()

            engine = create_engine("mysql+mysqlconnector://root:256984@localhost:3306/trabalho", echo=True, future=True)

            client = Client(id, fullname, email, phone, cpf, rg, True)
            bank(client)
            continue
        case 3:
            break


            