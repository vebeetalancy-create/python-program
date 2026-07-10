class BankAccount:
  
    def __init__(self, balance):
        self.balance = balance

    # function to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited:", amount)
        else:
            print("Invalid deposit amount.")

    # function to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient balance.")

    # function to display balance
    def display_balance(self):
        print("Current Balance:", self.balance)

initial_balance = float(input("Initial Balance: "))
account = BankAccount(initial_balance)
deposit_amount = float(input("Deposit Amount: "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Withdraw Amount: "))
account.withdraw(withdraw_amount)
account.display_balance()