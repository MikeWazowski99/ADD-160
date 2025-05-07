'''
Homework1
Name: Michael Tapia
github link: https://github.com/MikeWazowski99/ADD-160
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        # your code here
        self.name = name
        self.account = starting_amount
        pass
    
    def __repr__(self):
        # your code here
        return f"Bank_account(name='{self.name}', Account Balance={self.account})"
    
    def __str__(self):
        # your code here:
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"
    
    def deposit(self,amount):
        # your code here
        if amount > 0:
            self.account += amount
            return f"{amount} deposited. New balance: {self.account}"
        else:
            return "Please enter a positive number"
        pass
    
    def withdraw(self,amount):
        if amount <= 0:
            return "Please withdraw an amount greater than zero."
        elif amount > self.account:
            return "Insufficient Funds"
        else:
            self.account -= amount
            return f"{amount} withdrawn. New balance: {self.account}"
        pass

    def check_balance(self):
        return f"Balance: {self.account}"
        pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))