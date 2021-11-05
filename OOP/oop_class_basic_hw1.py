'''Bài tập về nhà buổi 1. 
Tạo class, khai báo thuộc tính, phương thức cơ bản'''

class BankAccount:
    
    """Lớp mô tả cho Bank account"""

    def __init__(self, account_number, account_name, balance):
        self._account_number = account_number
        self._account_name = account_name
        self.set_balance(balance)

    
    def get_account_number(self):
        return self._account_number

    def get_account_name(self):
        return self._account_name

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance > 0:
            self._balance = new_balance 
        else:
            print("Số tiền nhập vào không hợp lệ: ")

    
    def display(self):
        print(f"{self.get_account_name()} - {self.get_account_number()} - {self.get_balance()}")

    def withdraw(self, amount):

        if 0 < amount < self._balance:
            self._balance = self._balance - amount
            print("Tổng tiền còn lại", self._balance)
        else:
            print("Số tiền rút không hợp lệ")
        
    def deposit(self,amount):
        if amount > 0:
            self._balance = self._balance + amount
            print("Tổng tiền", self._balance)
        else:
            print("Cần nạp số tiền lớn hơn 0")


hangduong = BankAccount("111110008888", "Hangduong", 10000000)
hangduong.display()
hangduong.withdraw(1000000)
hangduong.deposit(2000)
