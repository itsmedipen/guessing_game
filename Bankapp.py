


class Customer:
    def __init__(self,name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self,amount):
        if amount <=0:
            print('Invalid amount')
            return
        self.balance += amount
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient balance')

    def check_balance(self):
        print(f'{self.name} balance is {self.balance}')

