'''
Homework8
Name: Michael Tapia
github link: https://github.com/MikeWazowski99/ADD-160/tree/main
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in account."):
        self.message = message
        super().__init__(self.message)



class InvalidAmountError(Exception):
    def __init__(self, message="Amount must be a positive number."):
        self.message = message
        super().__init__(self.message)
    

# Function to withdraw money
def withdraw_money(balance, amount):
    try:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise InvalidAmountError()
        
        if amount > balance:
            raise InsufficientFundsError()
        
        return balance - amount
    
    except InvalidAmountError:
        raise
    
    except InsufficientFundsError:
        raise
        
        
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest8.py'))

