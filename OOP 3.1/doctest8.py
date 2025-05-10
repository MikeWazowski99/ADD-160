>>> from homework8 import *
>>> withdraw_money(100,120)
InsufficientFundsError: Insufficient funds in account.
>>> withdraw_money(80,210)
InsufficientFundsError: Insufficient funds in account.
>>> withdraw_money(100,[])
InvalidAmountError: Amount must be a positive number.
>>> withdraw_money(100,-70)
InvalidAmountError: Amount must be a positive number.
>>> withdraw_money(100,20)
80
>>> withdraw_money(100,60)
40