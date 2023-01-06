import datetime, time
import threading


class Remote():
    """A class serving as a template for Nexus AC inverter remote"""
    def __init__(self):
        self.power = False
        # self.possible_modes = list(range(3))
        self.current_mode = 0
        self.current_temp = 24
        self.led_status = True
        self.turbo_status = True
        self.swing_status = True
        self.direct_status = False
        self.time = None
        self.timer_status = False
        self.fan_speed = 5
        self.direction = None

    def switch(self):
        """Remote method to control the activity the Air Condition"""
        self.power = not self.power
        print(f"Power: {self.power}")

    def mode(self):
        if self.power:
            next_mode = self.current_mode + 1
            if self.current_mode == 0 or next_mode > 2:
                self.fan_speed = 5
                self.current_temp = 24
                self.current_mode = 0
                print("Current Mode: Auto")
                print(f"Current Temp: {self.current_temp}")
                print(f"Fan Speed: {self.fan_speed}")
            else:
                if next_mode == 1:
                    self.current_temp = 17
                    self.fan_speed = 20
                    self.current_mode = next_mode
                    print("Current Mode: Cool")
                    print(f"Temp: {self.current_temp}")
                    print(f"Fan Speed: {self.fan_speed}")
                elif next_mode == 2:
                    self.current_temp = 30
                    self.fan_speed = 20
                    self.current_mode = next_mode
                    print("Current Mode: Warm")
                    print(f"Temp: {self.current_temp}")
                    print(f"Fan Speed: {self.fan_speed}")

    def temp_increase(self):
        """ Method to increase temperature"""
        if self.power and self.current_temp < 30:
            self.current_temp += 1

    def temp_decrease(self):
        """ Method to increase temperature"""
        if self.power and self.current_temp > 17:
            self.current_temp -= 1

    def fan_speed(self):
        """ Method to regulate fan speed"""
        if self.power:
            next_speed = self.fan_speed + 5
            if next_speed > 20:
                self.fan_speed = 5
                print(f"Fan Speed: {self.fan_speed}")
            else:
                self.fan_speed = next_speed
                print(f"Fan Speed: {self.fan_speed}")

    def led(self):
        """ Method to switch on/off AC led"""
        if self.power:
            self.led_status = not self.led_status
            print(f"Led: {self.led_status}")

    def turbo(self):
        """ Method to turn on AC turbo"""
        if self.power:
            self.turbo_status = True
            print("Turbo: ON")

    def swing(self):
        """ Method to turn on AC Swing"""
        if self.power:
            self.swing_status = True
            self.direct_status = False
            self.direction = None
            print(f"Swing: {self.swing_status}")

    def direct(self):
        """ Method to fixate AC flap and adjust its direction """
        if self.power:
            self.swing_status = False
            self.direct_status = True
            if not self.direction:  # Block to set initial direction to 45 on first call
                self.direction = 45  # Setting the direction to angle 45
            else:  # Block to only increase direction provided that a direction is already set
                next_direction = self.direction + 15
                if next_direction < 90:
                    self.direction = next_direction
                    print(f"Angle: {self.direction}")
                else:  # Block to return to angle 15 if direction/angle equals 90
                    self.direction = 15
                    print(f"Angle: {self.direction}")
