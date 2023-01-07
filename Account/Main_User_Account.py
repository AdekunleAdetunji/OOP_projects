# Script importing the account class and instantiating this class for various users
from account import Account

account_dic = {}  # Dictionary to hold account objects
identifier = 0

while True:
    print()
    print("Enter 'N' to create new account or 'S' to sign in")
    print("Enter 'Q' to exit")
    print()

    prompt = input()

    if prompt.lower() == 'n':  # Block to create new account
        name = input("Enter Username: ")
        password = input("Enter Password: ")
        deposit = int(input("Make a deposit: "))
        user_account = Account(name.title(), password, deposit)
        account_dic[identifier] = user_account
        print("Account creation successful")
        print(f"Your account number is {identifier}")
        print()
        print("Kindly sign into the account to start using your account")
        identifier += 1

    elif prompt.lower() == 's':  # Block to log a user in
        try:
            identifier = int(input("Enter your account number: "))
            password = input("Enter password: ")
            user = account_dic[identifier]

            if user.password != password:
                raise Exception("Invalid Password")
            else:
                while True:
                    print(f"Welcome {user.name}")
                    print()
                    print("Enter 'B' for balance check")
                    print("Enter 'W' for withdrawal")
                    print("Enter 'I' for account info")
                    print("Enter 'D' for deposit")
                    print("Enter 'Q' or any other key to quit")
                    print()

                    prompt = input()

                    if prompt.lower() == 'b':  # Condition to call the account object balance method
                        user.balance_check(password)
                    elif prompt.lower() == 'w':  # Condition to execute withdrawal from account
                        amount = input("Enter Amount: ")
                        user.withdraw(amount, password=password)
                    elif prompt.lower() == 'i':  # Condition to call account object info method
                        user.show(password)
                    elif prompt.lower() == 'd':  # Condition to call execute deposit into account object
                        amount = input("Enter Amount: ")
                        user.deposit(amount, password)
                    else:
                        print("Thanks for checking in, see you some other time")
                        break

                    # Prompt to confirm if another transaction need be done in account
                    print("Enter 'Y' to perform another transaction and 'N' to log out")
                    exit_prompt = input()
                    if exit_prompt.lower() != 'y':
                        break
        except KeyError:
            print("Account does not exist")
        except Exception as e:
            print("Invalid password")
    else:
        print("Thanks for checking in, hope to see you some other time.")
        break
