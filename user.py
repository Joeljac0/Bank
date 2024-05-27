#Sug mina bollar, denna kod är scrapad

"""
import pickle

#Parent Class
class User():
    def __init__(self, number: float, fname: str, ename: str, pincode: float):
        self.number = number
        self.fname = fname
        self.ename  = ename
        self.pincode = pincode

    def show_details(self):
        print("Personal Details\n")
        print("Number ", self.number)
        print("Name ", self.fname)
        print("Name ", self.ename)
        print("Pincode ", self.pincode)

    
#Child Class
class Bank(User):
    def __init__(self,fname, pincode):
        super().__init__(fname, pincode)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : Kornro", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : Kornro", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : Kornro", self.balance)
    
    def view_balance(self):
        self.show_details()
        print("Account balance: Kornro", self.balance)
"""