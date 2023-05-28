class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0, 0.01)

    def make_deposit(self, amount):
        self.account.deposit(amount)    

    def make_withdraw(self, withdraw):
        self.account.withdraw(withdraw) 

    def display_user_balance(self):
        self.account.display_account_info() 

class BankAccount:
    accounts = []

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, withdraw):
        if (self.balance - withdraw) >= 0:
            self.balance -= withdraw
        else: 
            print(f"Insufficient funds. Subtracting $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest_rate(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.interest_rate)

rainsaccount = User("Lorraine", "ruby@mail.com")


rainsaccount.make_deposit(30)
rainsaccount.display_user_balance()