"""BankAccount example demonstrating encapsulation and simple methods"""

class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self._balance = float(balance)  # protected attribute by convention

    @property
    def balance(self):
        return self._balance

    # def get_balance(self):
    #     return self._balance
    
    # def set_balance(self, new_balance):
    #     if new_balance < 0:
    #         raise ValueError("Balance cannot be negative")
    #     self._balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount



def create_account():
    name = input("Enter your name: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(name, initial_balance)
# print(account.get_balance())
# # account.set_balance(500)
# print*()
# print(account.get_balance())

account = create_account()


account.deposit(500)
print(account.balance)
account.withdraw(1500)
print(account.balance)