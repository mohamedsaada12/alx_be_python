import os

class BankAccount:
    def __init__(self, initial_balance=0):
        self.file = "balance.txt"
        self.account_balance = self._read_balance() or initial_balance

    def _read_balance(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                return float(f.read().strip())
        return None

    def _write_balance(self):
        with open(self.file, 'w') as f:
            f.write(str(self.account_balance))

    def deposit(self, amount):
        self.account_balance += amount
        self._write_balance()

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self._write_balance()
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
