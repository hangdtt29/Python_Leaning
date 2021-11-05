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
            raise ValueError("Sá»‘ dÆ° pháº£i lá»›n hÆ¡n 0")

    def display(self):
        print(
            f"| {self.account_number:9} | {self.account_name:15} | {self.balance:>15} |")

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Sá»‘ tiá»�n pháº£i lá»›n hÆ¡n 0 vĂ  khĂ´ng Ä‘Æ°á»£c vÆ°á»£t quĂ¡ sá»‘ dÆ° hiá»‡n táº¡i")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Sá»‘ tiá»�n pháº£i lá»›n hÆ¡n 0")

    @classmethod
    def from_csv(cls, csv_file):
        accounts = []

        with open(csv_file) as file:
            reader = csv.reader(file)

            for account_number, account_name, balance in reader:
                accounts.append(
                    cls(account_number, account_name, int(balance)))

        return accounts


csv_accounts = BankAccount.from_csv(csv_file)

print(f"| {'Number':9} | {'Account Name':15} | {'Balance':15} |")
print(f"|{'-' * 11}|{ '-' * 17 }|{'-' * 17}|")
for account in csv_accounts:
    account.display()