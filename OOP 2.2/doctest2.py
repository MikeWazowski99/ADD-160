>>> from homework2 import *
>>> a = SavingsAccount("bob",100)
>>> print(a)
Savings Account - bob: Balance = $100.00, Interest Rate = 1.0%
>>> a
SavingsAccount(account_holder='bob', balance=100, interest_rate=1.0%)
>>> a.apply_interest()
101.0
>>> a = SavingsAccount("bob",12345)
>>> a.apply_interest()
12468.45
>>> a = CheckingAccount("bob",100)
>>> print(a)
Checking Account - bob: Balance = $100.00, Overdraft Limit = $100.00
>>> a
CheckingAccount(account_holder='bob', balance=100, overdraft_limit=100.0)
>>> a.withdraw(-20)
Withdrawal amount must be positive.
>>> a.withdraw(230.0)
Withdrawal exceeds overdraft limit.
>>> a.withdraw(30)
70
>>> a = SavingsAccount("bob",12345)
>>> a.withdraw(130)
130 withdrawn. New balance: 12215
>>> a.withdraw(854.34)
854.34 withdrawn. New balance: 11360.66