"""
Gary Simmons
March 2018

Kata Description: You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""
import numpy as np

def sort_array(source_array):
    elements=len(source_array)
    if elements!=0:
        newArray=[0]*elements
    
    
        source_array=np.array(source_array)
        oddIndecies=np.where(source_array%2==1)
        oddlist=source_array[oddIndecies]
        sortedOdds=np.sort(oddlist)
    
        oddIndex=0
        sourceIndex=0
        for x in source_array:
            if x%2==1:
                newArray[sourceIndex]=sortedOdds[oddIndex]
                oddIndex=oddIndex+1
            else:
                newArray[sourceIndex]=source_array[sourceIndex]
            sourceIndex=sourceIndex+1
    else:
          newArray=[]
    return newArray
    # Return a sorted array.
