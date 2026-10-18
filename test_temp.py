from mymath import average, celsius_to_fahrenheit

def temp():
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37.5) == 95.5

def average():
    assert average([0.1, 0.2, 0.3]) == 0.2