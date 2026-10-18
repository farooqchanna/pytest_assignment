def square(n):
    return n * n

def is_even(n):
    return n % 2 == 0

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
def average(numbers):
    return sum(numbers) / len(numbers)

def is_leap_year(year):
    return year % 4 == 0 and (
        year % 100 != 0 or year % 400 == 0)