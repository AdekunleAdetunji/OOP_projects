# This is a script for a Dimmer switch class and the implementation code

class DimmerSwitch():
    """A class serving as the template for real life dimmer switch objects"""
    def __init__(self):
        self.switch_status = "OFF"
        self.brightness = 0

    def switch_on(self):
        """Switch on method"""
        self.brightness = 1
        self.switch_status = "ON"

    def switch_off(self):
        """Switch off method"""
        self.brightness = 0
        self.switch_status = "OFF"

    def increase(self, level):
        """Method to increase the object brightness"""
        projection = self.brightness + level
        if 0 < projection <= 11:
            self.brightness = projection
        else:
            print("Warning: Invalid input")

    def decrease(self, level):
        """Method to decrease object brightness"""
        projection = self.brightness - level
        if 0 <= projection < 11:
            self.brightness = projection
            if projection == 0:
                self.switch_off()
        else:
            print('Warning: Invalid input')

    def status(self):
        """Method to show the bulb status"""
        print()
        print(f"Switch status: {self.switch_status}")
        print(f"Switch brightness: {self.brightness}")


switch_1 = DimmerSwitch()
switch_1.status()
switch_1.switch_on()
switch_1.status()
switch_1.increase(4)
switch_1.status()
switch_1.decrease(2)
switch_1.status()
switch_1.decrease(3)
switch_1.status()
print(type(switch_1))