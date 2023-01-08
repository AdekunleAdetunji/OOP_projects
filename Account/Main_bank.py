# Main script that calls the Bank class
from bank import Bank

bank_obj = Bank('First_bank')

print(f"Welcome to {bank_obj.name}")

while True:
    try:
        print()
        print("Enter 'N' to create new account or 'M' to transact on an existing account")
        print("Enter 'Q' to exit")
        print()

        prompt = input()

        if prompt.lower() == 'n':
            bank_obj.new()

        elif prompt.lower() == 'm':
            print()
            print("Enter 'B' for balance check")
            print("Enter 'W' for withdrawal")
            print("Enter 'I' for account info")
            print("Enter 'D' for deposit")
            print("Enter 'C' to close an account")
            print("Enter 'Q' or any other key to quit")
            print()

            prompt = input()

            if prompt.lower() == 'b':
                bank_obj.balance()

            elif prompt.lower() == 'w':
                bank_obj.withdraw()

            elif prompt.lower() == 'i':
                bank_obj.account_info()

            elif prompt.lower() == 'd':
                bank_obj.deposit()

            elif prompt.lower() == 'c':
                bank_obj.close()

            elif prompt.lower() == 'q':
                print("Thanks for checking in, see you some other time")
                break

            else:
                print("Invalid input")
        else:
            print("Thanks for checking in, see you some other time")
            break
    except Exception as e:
        print(e)

print("Done")
