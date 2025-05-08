>>> from homework4 import *
>>> car1 = Car("Toyota", "Corolla")
>>> car2 = Car("Honda", "Civic")
>>> car1.display_info()
'Car: Toyota Corolla'
>>> car2.display_info()
'Car: Honda Civic'
>>> Car.update_total_cars(5)
>>> print(f"Total cars: {Car.total_cars}")
Total cars: 5
>>> Car.general_info()
'Cars are a mode of transportation.'
