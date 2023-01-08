# A class simulating a bank account

class Account():
    """A class simulating a bank account"""
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance

    def withdraw(self, amount):
        """ A method to execute withdrawal from account"""
        try:
            if amount.isnumeric() and self.balance < int(amount):
                raise Exception("Insufficient Funds")
            elif not amount.isnumeric() or int(amount) < 0:
                raise Exception("Invalid amount")
            else:
                print("Withdrawal Successful")
                self.balance -= int(amount)
        except Exception as e:
            print(e)

    def deposit(self, amount):
        """ Method to initiate deposit into user account """
        try:
            if amount.isnumeric() and int(amount) > 0:
                self.balance += int(amount)
                print("Deposit successful")
            else:
                raise Exception('Invalid Amount')
        except Exception as e:
            print(e)

    def balance_check(self):
        """ Method to check the balance in user account """
        print(f"Balance: {self.balance}")

    def show(self):
        """ Method to show account info"""
        print(f"Account Name: {self.name}")
        print(f"Account Balance: {self.balance}")

