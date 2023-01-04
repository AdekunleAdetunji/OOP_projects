#  This is a script emulating a basic user account with no functions

user = 'adetunji'  # Name on account
password = 12345  # Account password
balance = 500  # Account balance

while True:
    print('Welcome Dear User.')

    user_prompt = input("Please enter your username: ")
    password_prompt = input("Please enter your password: ")
    print(int(password_prompt))

    if user_prompt.lower() == user and int(password_prompt) == password:
        print(f"Welcome Mr. {user_prompt.lower()}")
        print("Enter 'B' to check account balance.")
        print("Enter 'T' to transfer to another account")
        print("Enter 'W' to withdraw funds")
        print("Enter 'D' to make deposit into your account")
        print("Enter 'Q' log out of your account")
        action_prompt = input()  # Prompt for user input

        if action_prompt.lower() == "b":
            print(balance)

        elif action_prompt.lower() == "w":
            amount_prompt = input("Please enter the amount you will like to withdraw: ")
            if int(amount_prompt) > balance:
                print("Insufficient funds")
            elif int(amount_prompt) <= 0:
                print("Kindly enter an amount greater than zero")
            else:
                print("Withdrawal successful")
                balance -= int(amount_prompt)

        elif action_prompt.lower() == "d":
            amount_prompt = input("Please enter the amount you want to deposit: ")
            if int(amount_prompt) <= 0:
                print("Kindly enter an amount greater than zero")
            else:
                print("Deposit was successful.")
                balance += int(amount_prompt)

        elif action_prompt.lower() == 't':
            amount_prompt = input("How much do you want to transfer? ")
            if int(amount_prompt) <= 0:
                print("Kindly enter an amount greater than zero")
            else:
                reciever_account_prompt = input("Kindly provide the destination account: ")
                print("Transfer successful")
                balance -= int(amount_prompt)

        else:
            print('Thanks for checking in.')
            break

    else:
        print('Kindly enter the correct info.')
        break
