>>> from homework1 import *
>>> a = Bank_Account("Bob",100)
>>> type(a.account) == int
True
>>> a
Bank_Account(name='Bob', Account Balance=100)
>>> print(a)
Account Name: Bob
Account Balance: 100
>>> a.deposit(150)
150 deposited. New balance: 250
>>> a.deposit(-30)
Please deposit a positive number.
>>> a.withdraw(200)
200 withdrawn. New balance: 50
>>> a.withdraw(70)
Insufficient funds.
>>> a.withdraw(-90)
Please withdraw an amount greater than zero.
>>> a.check_balance()
Balance: 50
