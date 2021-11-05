
"""Khai báo class SavingAccount kế thừa từ BankAccount"""
class BankAccount:
    minimum_balance = 50000

    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self._owner = owner
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def owner(self):
         return self._owner
        

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(f"{'Account Information'}")
        self.owner.get_info()
        print(f"| {self.account_number} | {self.balance} |")

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Số tiền rút phải lớn hơn 0 và không vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")


class SavingAccount(BankAccount):
    monthly_interest_rate = 0.005

    def __init__(self, account_number, owner, balance=0):
        super().__init__(account_number, owner, balance=balance)
    
    # Tiền lãi hàng tháng
    @property
    def calculate_interest(self):
        interest = self.balance * self.monthly_interest_rate
        return interest


class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
        
    def get_info(self):
        print(
            f"| {self.name:9} | {self.date_of_birth:9} | {self.email:9} | {self.phone:15}")

hangduong = Customer("Hangduong", "01/01/1993", "hangduong@gmail.com", "0912345666")
bankaccount_hangduong = BankAccount("0111188888", hangduong, 999999900)
bankaccount_hangduong.display()
