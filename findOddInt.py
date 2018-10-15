"""
Gary Simmons
March 2018
Kata Prompt Description: Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""
def find_it(seq):
    for x in seq:
        count=seq.count(x)
        if count%2==1:
            value=x
    return value
