>>> from homework6 import *
>>> a = Device("Device1")
>>> a.turn_on()
Device1 is now ON.
>>> a.turn_off()
Device1 is now OFF.
>>> a = Light("Device1")
>>> a.set_brightness(30)
Device1 brightness set to 30.
>>> a.set_brightness(90)
Device1 brightness set to 90.
>>> a.set_brightness(125)
Invalid brightness level. Must be between 0 and 100.
>>> a = Light("Device2")
>>> a.set_brightness(45)
Device2 brightness set to 45.
>>> a.turn_off()
Device2 is now OFF.
>>> a = LEDLight("Device3")
>>> a.set_color("Blue")
Device3 color changed to Blue.
>>> a.set_color("Yellow")
Device3 color changed to Yellow.
>>> a.set_brightness(78)
Device3 brightness set to 78.
>>> a = SmartBulb("Device4")
>>> a.turn_on()
Device4 is now ON.
>>> a.enable_smart_mode()
Device4 smart mode enabled.
>>> a.disable_smart_mode()
Device4 smart mode disabled.
>>> a.set_brightness(62)
Device4 brightness set to 62.
