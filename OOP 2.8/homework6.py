'''
Homework6
Name: Michael Tapia
github link: https://github.com/MikeWazowski99/ADD-160/tree/main
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Device:
    def __init__(self, name):
        self.name = name
        #Makes sure that the default is false
        self.status = False
        pass

    def turn_on(self):
        #turns on function
        self.status = True
        print(f"{self.name} is now ON.")
        pass

    def turn_off(self):
        #turns off function
        self.status = False
        print(f"{self.name} is now OFF.")
        pass

class Light(Device):
    def __init__(self, name, brightness=50):
        super().__init__(name)
        self.brightness = brightness
        pass
    
    def set_brightness(self, level):
        #sets the brightness lvl using a num
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.name} brightness set to {level}.")
        else:
            print("Invalid brightness level. Must be between 0 and 100.")
        pass

class LEDLight(Light):
    def __init__(self, name, brightness=50, color="White"):
        super().__init__(name,brightness)
        self.color = color
        pass
    
    def set_color(self, color):
        self.color = color
        print(f"{self.name} color changed to {color}.")
        pass

class SmartBulb(Light):
    def __init__(self, name, brightness=50, smart_mode=False):
        super().__init__(name, brightness)
        self.smart_mode = smart_mode
        pass
    
    def enable_smart_mode(self):
        self.smart_mode = True
        print(f"{self.name} smart mode enabled.")
        pass
    
    def disable_smart_mode(self):
        self.smart_mode = False
        print(f"{self.name} smart mode disabled.")
        pass

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest6.py'))

