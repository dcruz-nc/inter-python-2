from BankAccount import BankAccount

account = BankAccount("David Cruz's Account", 50500)

account.deposit(600)

account.withdraw(100)

print(account.get_balance())