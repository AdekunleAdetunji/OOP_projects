#  Bank class
from account import Account


class Bank():
    """ A class that models a bank """
    def __init__(self, name):
        """ Initializes the bank with the accounts as well as next accounts"""
        self.accounts = {}
        self.next_account = 0
        self.name = name

    def new(self):
        """ Method that creates an instance of the Account class and adds it to the\
        bank accounts """
        name = input("Name: ")
        password = input("Password: ")
        starting_balance = input("Make first deposit: ")
        # Condition to check if balance > 0
        if int(starting_balance) < 0 or not starting_balance.isnumeric():
            raise Exception("Invalid starting balance")
        account_obj = Account(name, password, int(starting_balance))
        self.accounts[self.next_account] = account_obj
        self.next_account += 1

    def balance(self):
        """ Method to check account balance"""
        account_num = input("Enter account number: ")
        # Exception to raise error for invalid account number
        if not account_num.isnumeric():
            raise Exception("Invalid account number")
        if int(account_num) not in self.accounts.keys():
            raise Exception("Account number not in database")
        account_obj = self.accounts[int(account_num)]
        password = input("Enter Password: ")
        if password != account_obj.password:  # Exception to check for correct password
            raise Exception("invalid password")
        account_obj.balance_check()

    def withdraw(self):
        """ A method to initiate withdrawal from account"""
        account_num = input("Enter account number: ")
        if not account_num.isnumeric():
            raise Exception("Account number can only be numbers")
        if int(account_num) not in self.accounts.keys():
            raise Exception("Account number not in database")
        account_obj = self.accounts[account_num]
        password = input("Enter password: ")
        if password != account_obj.password:
            raise Exception("Invalid password")
        print(f"Welcome {account_obj.name}")
        amount = input("Enter withdrawal amount: ")
        account_obj.withdraw(amount)

    def deposit(self):
        """ Method to make deposit into account"""
        account_num = input("Enter account number: ")
        if not account_num.isnumeric():
            raise Exception("Invalid account number")
        if int(account_num) not in self.accounts.keys():
            raise Exception("Account number not in database")
        account_obj = self.accounts[account_num]
        password = input("Enter password: ")
        if password != account_obj.password:
            raise Exception("Invalid password")
        print(f"Welcome {account_obj.name}")
        amount = input("Enter deposit amount: ")
        account_obj.deposit(amount)

    def close(self):
        """ Method to close down bank account """
        account_num = input("Enter account number: ")
        if not account_num.isnumeric():
            raise Exception("Invalid account number")
        if int(account_num) not in self.accounts.keys():
            raise Exception("Account number not in database")
        account_obj = self.accounts[account_num]
        password = input("Enter password: ")
        if password != account_obj.password:
            raise Exception("Invalid password")
        account_obj.balance_check()
        del self.accounts[account_num]

    def account_info(self):
        """ Method to return account info """
        account_num = input("Enter account number: ")
        if not account_num.isnumeric():
            raise Exception("Invalid account number")
        if int(account_num) not in self.accounts.keys():
            raise Exception("Account number not in database")
        account_obj = self.accounts[account_num]
        password = input("Enter password: ")
        if password != account_obj.password:
            raise Exception("Invalid password")
        account_obj.show()
