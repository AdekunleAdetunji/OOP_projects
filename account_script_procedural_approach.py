# This is a script showing basic bank account actions using functions
import sys


user = 'wilsonian'
password = 12345
balance = 500


def login():
    """ A function to control user login"""
    global user, password
    try:
        for i in range(4, -1, -1):  # A loop to prevent not more than 5 login attempts
            username = input("Enter Username: ")
            secret = int(input("Enter Secret: "))
            if username.lower() == user and password == secret:
                print("Login successful!")
                print(f"Welcome {username}!")
                break
            elif i == 0:
                raise Exception("Login attempt exceeded, try again in 24hrs")
            else:
                print("Please enter a valid login Info")
    except Exception as e:
        print(e)
        sys.exit()


def balance_check():
    """A function to help retrieve user account balance."""
    global balance
    print(f"Your account balance is ${balance}")


def withdraw():
    """ A function to execute withdrawal from account"""
    global balance
    amount = int(input("Enter withdrawal amount: "))
    if 0 < amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
        print("Please remove your card!")
    elif amount > balance:
        print("Insufficient funds!")
    else:
        print("Error: Invalid withdrawal amount")


def transfer():
    """ A function to transfer funds from one account to another"""
    global balance
    amount = int(input("Enter transfer amount: "))
    input("Enter recipient account: ")
    if 0 < amount < balance:
        balance -= amount
        print("Transfer successful")
        print("Please take your card")
    elif amount > balance:
        print("Insufficient Funds")
    else:
        print("Error: Invalid transfer amount.")


def deposit():
    """A function to initiate deposit into user account"""
    global balance
    amount = int(input("Enter deposit amount: "))
    if 0 < amount:
        balance += amount
        print("Deposit was successful, please take your card")
    else:
        print("Invalid deposit amount")


login()

while True:
    """ A loop to perform action on account"""
    print()
    print(f"Welcome {user}")
    print("Enter 'B' to check account balance.")
    print("Enter 'T' to transfer to another account")
    print("Enter 'W' to withdraw funds")
    print("Enter 'D' to make deposit into your account")
    print("Enter 'Q' log out of your account")
    print()

    prompt = input()  # Prompt to take user input

    if prompt.lower() == 'b':
        balance_check()
    elif prompt.lower() == 't':
        transfer()
    elif prompt.lower() == 'w':
        withdraw()
    elif prompt.lower() == 'd':
        deposit()
    else:
        print("Thank for checking in, hope to see you again!")
        break

    extra_action = input("Enter 'Y' for another action and any key to logout")

    if extra_action.lower() == 'y':
        continue
    else:
        print('Logout successful')
        break
