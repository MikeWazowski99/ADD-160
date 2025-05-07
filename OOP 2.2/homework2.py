'''
Homework2
Name: Michael Tapia
github link: https://github.com/MikeWazowski99/ADD-160
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self,name,starting_amount,interest_rate=1.0):
        # your code here
        self.name=name
        self.account = starting_amount
        self.interest_rate = interest_rate
        #self.overdraft = overdraft_limit
    
    def __repr__(self):
        # your code here
        # Prints out a message while using the init that was made at the beginning of the class
        return f"Bank_Account(name='{self.name}', Account Balance={self.account}, Interest Rate={self.interest_rate})"
    
    def __str__(self):
        # your code here:
        # Prints out a message while using the init that was made at the beginning of the class
        return f"Account Name: {self.name}\nAccount Balance: {self.account}, Interest Rate:{self.interest_rate}"
    
    # Deposit stuff that makes it so that you can only deposit a positive number and it will tell the user the new balance everytime a deposit is made
    def deposit(self,amount):
        # your code here
        if amount>0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print(f"Please deposit a positive number.")
    
    # Withdraw function that makes it so you can only withdraw from a number that is greater than zero and if there isnt enough amount in the balance then it will tell the user insufficient funds
    def withdraw(self,amount):
        if amount>0:
            if self.account-amount>=0:
                self.account-=amount
                print(f"{amount} withdrawn. New balance: {self.account}")
            else:
                print(f"Insufficient funds.")
        else:
            print(f"Please withdraw an amount greater than zero.")

    
    def check_balance(self):
        """
        Check and return the balance of the account holder's account.
        """
        print(f"Balance: {self.account}")

class SavingsAccount(Bank_Account):
    def __init__(self, name, starting_amount, interest_rate=1.0):
        super().__init__(name, starting_amount, interest_rate)
    
    # Prints out a message while using the init that was made at the beginning of the class
    def __repr__(self):
        return  f"Savings Acount: (name='{self.name}', Account Balance={self.account}, Interest Rate={self.interest_rate})"
    
    # Prints out a message while using the init that was made at the beginning of the class
    def __str__(self):
        return f"Savings Account: {self.name}: Balance = ${self.account:.2f}, Interest Rate = {self.interest_rate}%"
    
    def apply_interest(self):
        # function that will apply the interest rate
        interest =self.account * (self.interest_rate / 100)
        self.account += interest
        return self.account
    pass

class CheckingAccount(Bank_Account):
    def __init__(self, name, starting_amount, overdraft_limit=100.0):
        super().__init__(name, starting_amount, overdraft_limit)
        self.overdraft_limit = overdraft_limit
    # Prints out a message while using the init that was made at the beginning of the class    
    def __repr__(self):
        return f"Checking Account:(account_holder='{self.name}', balance={self.account}, overdraft_limit={self.overdraft_limit})"
    
    # Prints out a message while using the init that was made at the beginning of the class
    def __str__(self):
        return f"Checking Account - {self.name}: Balance = ${self.account:.2f}, Overdraft Limit = ${self.overdraft_limit}"
    
    def withdraw(self, amount):
        #function that only allows withdrawals that are a positive number and if the amount withdrawn is greater than the amount in the bank account then it will tell the user theres an overdraft limit
        if amount <= 0:
            print("Withdrawal must be a positive number")
            return None
        elif amount > (self.account + self.overdraft_limit):
            print("Withdrawal exceeds overdraft limit.")
            return None
        else:
            self.account -= amount
            return self.account
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))