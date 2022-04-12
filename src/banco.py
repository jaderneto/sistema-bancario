from src.conta import *
from src.person import *


flag = True
accounts = []


def search_account(s):
    for i in accounts:
        if i.owner.cpf == s:
            return i


while flag:
    print("------------ WELCOME TO BANK SYSTEM ---------------")
    print("Choose one option:")
    print("1 - EXIT")
    print("2 - CREATE NEW ACCOUNT")
    print("3 - SEARCH FOR ACCOUNT")
    print("4 - MAKE A DEPOSIT")
    print("5 - MAKE A WITHDRAW")
    print("6 - SHOW ACCOUNT MOVIMENTS")

    opt = int(input("Opção: "))

    if opt == 1:
        flag = False
        print("See you soon!")
    elif opt == 2:
        print("--- NEW ACCOUNT ---")
        name = str(input("Name: "))
        cpf = str(input("CPF: "))
        gender = str(input("Gender: "))

        p = Person(name, cpf, gender)
        new = Conta(p)
        accounts.append(new)
        print("Account created!!!")
        new.getinfo()

    elif opt == 3:
        s3 = str(input("What is the CPF of the account's owner? "))
        c3 = search_account(s3)
        c3.getinfo()

    elif opt == 4:
        s4 = str(input("What is the CPF of the account's owner? "))
        c4 = search_account(s4)
        v4 = float(input('What value do you want to deposit? '))
        c4.deposit(v4)

    elif opt == 5:
        s5 = str(input("What is the CPF of the account's owner? "))
        c5 = search_account(s5)
        v5 = float(input('What value do you want to withdraw? '))
        c5.withdraw(v5)

    elif opt == 6:
        s6 = str(input("What is the CPF of the account's owner? "))
        c6 = search_account(s4)
        c6.show_moviments()
