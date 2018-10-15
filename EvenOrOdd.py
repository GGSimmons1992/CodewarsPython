"""
Gary Simmons
March 2018

Kata Description:Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""
def even_or_odd(number):
    if number%2==0:
        value='Even'
    else:
        value='Odd'
    return value
