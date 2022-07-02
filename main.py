from account import Account
from sqlalchemy import create_engine
from sqlalchemy import text
from random import randint

while True:

    print("Type 1 to sign in, 2 to register, 3 to stop")
    m = int(input())

    match m:
        case 2:
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
            print("Please insert a passcode")
            passcode = input()
            id = randint(000000, 999999)

            engine = create_engine("mysql+mysqlconnector://root:256984@localhost:3306/trabalho", echo=True, future=True)

            with engine.connect() as conn:
                conn.execute(
                    text("INSERT INTO client (idClient, passcode, fullname, email, phone, cpf, rg) VALUES (:id, :passcode, :fullname, :email, :phone, :cpf, :rg)"),
                    [{"id": id, "passcode": passcode, "fullname": fullname, "email": email, "phone": phone, "cpf": cpf, "rg": rg}]
                )
                conn.commit()

            acc = Account(passcode, fullname, email, phone, cpf, rg)
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
        