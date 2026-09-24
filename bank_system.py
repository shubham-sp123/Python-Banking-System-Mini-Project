
import random
from datetime import datetime

accounts = {}   


def create_account():
    print("\n--- CREATE ACCOUNT ---")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    pin = input("Set a 4 digit pin: ")
    while len(pin) != 4 or pin.isdigit() == False:
        print("Pin should be 4 digits only")
        pin = input("Set a 4 digit pin: ")

    acc_no = random.randint(100000, 999999)
    while acc_no in accounts:
        acc_no = random.randint(100000, 999999)

    accounts[acc_no] = {
        'name': name,
        'phone': phone,
        'pin': pin,
        'balance': 0,
        'history': []
    }

    print("Account created successfully")
    print("Your account number is", acc_no)
    print("Please note it down, you will need it to login")


def login():
    print("\n--- LOGIN ---")
    acc_no = input("Enter account number: ")

    if acc_no.isdigit() == False or int(acc_no) not in accounts:
        print("Account does not exist")
        return None

    acc_no = int(acc_no)
    pin = input("Enter pin: ")

    if accounts[acc_no]['pin'] == pin:
        print("Login successful. Welcome", accounts[acc_no]['name'])
        return acc_no
    else:
        print("Wrong pin")
        return None


def check_balance(acc_no):
    print("Your balance is:", accounts[acc_no]['balance'])


def deposit(acc_no):
    amt = float(input("Enter amount to deposit: "))
    accounts[acc_no]['balance'] = accounts[acc_no]['balance'] + amt

    time_now = datetime.now().strftime("%d/%m/%Y %H:%M")
    accounts[acc_no]['history'].append(time_now + " - Deposited " + str(amt))

    print("Amount deposited. New balance =", accounts[acc_no]['balance'])


def withdraw(acc_no):
    amt = float(input("Enter amount to withdraw: "))

    if amt > accounts[acc_no]['balance']:
        print("Not enough balance")
    else:
        accounts[acc_no]['balance'] = accounts[acc_no]['balance'] - amt
        time_now = datetime.now().strftime("%d/%m/%Y %H:%M")
        accounts[acc_no]['history'].append(time_now + " - Withdrew " + str(amt))
        print("Amount withdrawn. New balance =", accounts[acc_no]['balance'])


def transfer(acc_no):
    to_acc = input("Enter account number to transfer to: ")

    if to_acc.isdigit() == False or int(to_acc) not in accounts:
        print("Account not found")
        return

    to_acc = int(to_acc)

    if to_acc == acc_no:
        print("You cannot transfer to your own account")
        return

    amt = float(input("Enter amount: "))

    if amt > accounts[acc_no]['balance']:
        print("Not enough balance")
        return

    accounts[acc_no]['balance'] = accounts[acc_no]['balance'] - amt
    accounts[to_acc]['balance'] = accounts[to_acc]['balance'] + amt

    time_now = datetime.now().strftime("%d/%m/%Y %H:%M")
    accounts[acc_no]['history'].append(time_now + " - Sent " + str(amt) + " to " + str(to_acc))
    accounts[to_acc]['history'].append(time_now + " - Received " + str(amt) + " from " + str(acc_no))

    print("Transfer done")


def show_history(acc_no):
    print("\n--- TRANSACTION HISTORY ---")
    if len(accounts[acc_no]['history']) == 0:
        print("No transactions yet")
    else:
        for h in accounts[acc_no]['history']:
            print(h)


def change_pin(acc_no):
    old = input("Enter old pin: ")
    if old != accounts[acc_no]['pin']:
        print("Wrong pin")
        return

    new = input("Enter new pin: ")
    confirm = input("Confirm new pin: ")

    if new == confirm:
        accounts[acc_no]['pin'] = new
        print("Pin changed successfully")
    else:
        print("Pins don't match")


def account_menu(acc_no):
    while True:
        print("\n1.Check Balance  2.Deposit  3.Withdraw  4.Transfer  5.History  6.Change Pin  7.Logout")
        ch = input("Enter choice: ")

        if ch == '1':
            check_balance(acc_no)
        elif ch == '2':
            deposit(acc_no)
        elif ch == '3':
            withdraw(acc_no)
        elif ch == '4':
            transfer(acc_no)
        elif ch == '5':
            show_history(acc_no)
        elif ch == '6':
            change_pin(acc_no)
        elif ch == '7':
            print("Logging out...")
            break
        else:
            print("Wrong choice, try again")



while True:
    print("\n===== BANKING SYSTEM =====")
    print("1.Create Account  2.Login  3.Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        create_account()
    elif ch == '2':
        acc = login()
        if acc != None:
            account_menu(acc)
    elif ch == '3':
        print("Thank you for using Banking System")
        break
    else:
        print("Wrong choice, try again")
