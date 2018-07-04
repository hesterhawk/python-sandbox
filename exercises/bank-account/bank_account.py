import threading

class BankAccount(object):
    def __init__(self):
        self.semaphore = threading.Lock()
        pass

    def get_balance(self):
        with self.semaphore:
            if not hasattr(self, 'amount'): raise ValueError
        
            return self.amount            

    def open(self):
        self.amount = 0

    def deposit(self, amount):
        with self.semaphore:
            if not hasattr(self, 'amount') or amount < 0: raise ValueError
        
            self.amount += amount

    def withdraw(self, amount):
        with self.semaphore:
            if not hasattr(self, 'amount'): raise ValueError
            if amount > self.amount or amount < 0: raise ValueError

            self.amount -= amount

    def close(self):
        del self.amount