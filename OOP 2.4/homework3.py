'''
Homework3
Name: Michael Tapia
github link: https://github.com/MikeWazowski99/ADD-160/tree/main
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Decorator:
    def __init__(self,func):
        self.func = func
        pass

    def __call__(self, *args, **kwds):
        result = 1
        if args:
            n = args[0]
        else:
            n = 1

        for i in range(1, n + 1):
            result *= i
            print(f"Factorial product = {result}. Currently multiplying by {i}")
        return result
        pass
#Decorator basically modifys or extends what a function does without changing its original code
@Decorator
def factorial(n):
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))