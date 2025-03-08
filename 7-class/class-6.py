class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds"
    
    def get_balance(self):
        return f"{self.owner}'s balance: {self.balance}"

# 創建物件
account = BankAccount("John", 1000)

# 使用方法
print(account.deposit(500))      # 輸出: Deposited 500. New balance: 1500
print(account.withdraw(200))     # 輸出: Withdrew 200. New balance: 1300
print(account.get_balance())     # 輸出: John's balance: 1300\
