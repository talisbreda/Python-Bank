from account import Account
from client import Client
from sqlalchemy import create_engine
from sqlalchemy import text
from random import randint
from cryptography.fernet import Fernet
<<<<<<< HEAD

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

def authenticate(email, password):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT passcode FROM client WHERE email = :email"),
            [{"email": email}]
        )
        conn.commit()
    passcode = bytes(result.scalar(), 'UTF-8')
    decPasscode = fernet.decrypt(passcode).decode()
    if decPasscode == password:
        accessUser(email)

def accessUser(email):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT fullname, phone, cpf, rg FROM client WHERE email = :email")
            [{"email": email}])
        conn.commit()
    
    print(result.all())

=======
>>>>>>> c5f44e4d63bdd48c79ed8fdd53c8b3b7f9c6b0b8

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
<<<<<<< HEAD
            passcode = fernet.encrypt(input().encode())
            
            createNewClient()
=======
            password = input()

            key = Fernet.generate_key()
            fernet = Fernet(key)
            passcode = fernet.encrypt(password.encode())

            id = randint(000000, 999999)

            engine = create_engine("mysql+mysqlconnector://root:256984@localhost:3306/trabalho", echo=True, future=True)

            with engine.connect() as conn:
                conn.execute(
                    text("INSERT INTO client (idClient, passcode, fullname, email, phone, cpf, rg) VALUES (:id, :passcode, :fullname, :email, :phone, :cpf, :rg)"),
                    [{"id": id, "passcode": passcode, "fullname": fullname, "email": email, "phone": phone, "cpf": cpf, "rg": rg}]
                )
                conn.commit()

>>>>>>> c5f44e4d63bdd48c79ed8fdd53c8b3b7f9c6b0b8
            acc = Client(passcode, fullname, email, phone, cpf, rg)
            continue
        case 3:
            break


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
        