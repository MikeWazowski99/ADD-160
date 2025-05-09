'''
Homework4
Name: Michael Tapia
github link: https://github.com/MikeWazowski99/ADD-160/tree/main
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class BakeryItem:
    """Abstract class representing a bakery item."""
    
    def __init__(self, size, flavor):
        self.size = size
        self.flavor = flavor
        self.add_ins = []
    
    def add_add_ins(self, add_in):
        """Abstract method to add an ingredient to the item."""
        self.add_ins.append(add_in)
        print(f"Added {add_in} to the {self.__class__.__name__.lower()}.")
        #pass

    def get_description(self):
        """Abstract method to get the item description."""
        raise NotImplementedError("TESTING")
        #pass

class Croissant(BakeryItem):
    """Concrete class representing a croissant."""
    
    def add_add_ins(self, add_in):
        super().add_add_ins(add_in)
        #pass
    
    def get_description(self):
        base = f"{self.size} {self.flavor} croissant"
        if self.add_ins:
            return f"{base} with {', '.join(self.add_ins)}."
        return f"{base}."
        #pass

class Muffin(BakeryItem):
    """Concrete class representing a muffin."""
    
    def add_add_ins(self, add_in):
        super().add_add_ins(add_in)
        #pass
    
    def get_description(self):
        base = f"{self.size} {self.flavor} muffin"
        if self.add_ins:
            return f"{base} with {', '.join(self.add_ins)}."
        return f"{base}."
        #pass


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest5.py'))

