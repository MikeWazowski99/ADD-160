'''
Homework4
Name:
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Car:
    # Class variable
    total_cars = 0
    
    
    def __init__(self, brand, model):
        """Initialize instance variables."""
        self.brand = brand
        self.model = model
        pass
    
    def display_info(self):
        """Instance method to display car details."""
        return f"Car: {self.brand} {self.model}"
        #pass
    
    @classmethod
    def update_total_cars(cls, count):
        """Class method to update total number of cars."""
        cls.total_cars = count
        #pass
    
    @staticmethod
    def general_info():
        """Static method providing general information about cars."""

        return "Cars are a mode of transportation."
        #pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py'))

