class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Funds cannot go below 0.")

    def get_balance(self):
        return "{self.account_name} has a balance of {self.balance}"
