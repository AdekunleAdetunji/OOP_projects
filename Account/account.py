# A class simulating a bank account

class Account():
    """A class simulating a bank account"""
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance

    def withdraw(self, amount, password):
        """ A method to execute withdrawal from account"""
        try:
            if password == self.password:
                if amount.isnumeric() and self.balance < int(amount):
                    raise Exception("Insufficient Funds")
                elif not amount.isnumeric() or int(amount) < 0:
                    raise Exception("Invalid amount")
                else:
                    print("Withdrawal Successful")
                    self.balance -= int(amount)
            else:
                raise Exception("Invalid Password")
        except Exception as e:
            print(e)

    def deposit(self, amount, password):
        """ Method to initiate deposit into user account """
        try:
            if self.password == password:
                if amount.isnumeric() and int(amount) > 0:
                    self.balance += int(amount)
                    print("Deposit successful")
                else:
                    raise Exception('Invalid Amount')
            else:
                raise Exception("Invalid Password")
        except Exception as e:
            print(e)

    def balance_check(self, password):
        """ Method to check the balance in user account """
        try:
            if self.password == password:
                print(f"Balance: {self.balance}")
            else:
                raise Exception("Invalid Password")
        except Exception as e:
            print(e)

    def show(self, password):
        """ Method to show account info"""
        try:
            if self.password == password:
                print(f"Account Name: {self.name}")
                print(f"Account Balance: {self.balance}")
            else:
                raise Exception("Invalid Password")
        except Exception as e:
            print(e)