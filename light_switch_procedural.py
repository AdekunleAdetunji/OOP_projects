# A python script uses procedural approach to model light bulb actions
switch_status = "Off"


def switch_on():
    """ A function to switch on a light bulb"""
    global switch_status
    switch_status = "On"


def switch_off():
    """A function to switch off a light bulb"""
    global switch_status


print(f"Light is currently {switch_status}")
switch_on()
print(f"Light is now {switch_status}")
