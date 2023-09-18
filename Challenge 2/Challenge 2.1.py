class BankAccount:
  
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
    
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
    else:
      print("Invalid deposit amount.")
     
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdrew ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
    else:
      print("Invalid withdraw amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}".format(self.__account_holder_name, self.__account_number, self.__account_balance))
account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_number, account_holder_name, initial_balance)
account.display_balance()
deposit_amount = float(input("Enter the deposit amount: "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter the withdrawal amount: "))
account.withdraw(withdraw_amount)
account.display_balance()
