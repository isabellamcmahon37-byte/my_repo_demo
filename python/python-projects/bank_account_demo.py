from bank_account import BankAccount

account1 = BankAccount("123", 100)
print(account1)

account1.deposit(100)
print(account1)

account1.withdraw(200)
print(account1)

print(account1.get_balance()) 