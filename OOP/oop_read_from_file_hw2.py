""" Bài 1: Nạp dữ liệu từ file csv, json """

import os
import sys
import csv
import json

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
csv_file = os.path.join(current_dir, "bank_accounts.csv")
json_file = os.path.join(current_dir, "bank_accounts.json")


class BankAccount:
    minimum_balance = 50000

    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError(" Số dư phải lớn hơn 0")

    def display(self):
        print(
            f"| {self.account_number:9} | {self.account_name:15} | {self.balance:>15} |")

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")

    @classmethod
    def from_csv(cls, csv_file):
        accounts = []

        with open(csv_file) as file:
            reader = csv.reader(file)

            for account_number, account_name, balance in reader:
                accounts.append(
                    cls(account_number, account_name, int(balance)))

        return accounts
        
    @classmethod
    def from_json(cls, jsonfile):
        accounts = []
        with open(jsonfile) as file:
            reader = json.load(file)

            for dict in reader:
                print(type(dict))
                accounts.append(cls(**dict))
    
        return accounts

# magic method print account
    def __str__(self):
        infor_account = f"| {self.account_number:9} | {self.account_name:15} | {self.balance:>15} |"
        return infor_account

csv_accounts = BankAccount.from_csv(csv_file)
json_accounts = BankAccount.from_json(json_file)

print(f"| {'Number':9} | {'Account Name':15} | {'Balance':15} |")
print(f"|{'-' * 11}|{ '-' * 17 }|{'-' * 17}|")
for account in csv_accounts:
    account.display()

for account in json_accounts:
    #account.display()
    print(account)


"""Bài 2: Magic method"""

#Tạo class Fraction (phân số)
class Fraction:

    def __init__(self, nr, dr):
        if dr == 0:
            raise ZeroDivisionError("Mẫu số phải lớn hơn 0")
        if dr < 0:
            self.nr = -1*nr
            self.dr = -1*dr
        else: 
            self._nr = nr
            self._dr = dr
        self.reduce()

        
    @property
    def nr(self):
        return self._nr

    @nr.setter
    def nr(self, nr):
        self._nr = nr
       
    @property
    def dr(self):
        return self._dr

    @dr.setter
    def dr(self, dr):
        self._dr = dr


    def __str__(self):
        if self.nr == 0:
            return "0"
        else:
            if self.dr == 1:
                return str(self.nr)
            else:
                return f"{self.nr}/{self.dr}"

    def hcf(self):
        '''Tìm ước chung lớn nhất của tử số và mẫu số'''
        nr = self.nr
        dr = self.dr
        if dr < 0:
            dr = dr*-1
        if nr < 0:
            nr = nr*-1
        if dr == 0 or nr == 0:
            return dr + nr
        else:
            while(nr != dr):
                if(nr > dr):
                    nr -= dr
                else:
                    dr -= nr
            return nr

    
    def reduce(self):

        re = self.hcf()
        self.dr = int(self.dr/re)
        self.nr = int(self.nr/re)

        

    def __add__(self,other):
        if type(other) == int or type(other) == float:
            return Fraction(self.nr + other * self.dr, self.dr)
        else: 
            nr = self.nr * other.dr + self.dr * other.nr
            dr = self.dr * other.dr
            return Fraction(nr,dr)
 
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) - (other.nr * self.dr), self.dr * other.dr)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.dr, other.nr * self.dr)


fr = Fraction(1, 2)
other = Fraction(4, -3)

print(fr + other)
print(fr - other)
print(fr * other)
print(fr / other)

print()

fr = Fraction(1, 2)
print(fr + 3)
print(fr - 7)
print(fr * 5)
print(fr / 2)

