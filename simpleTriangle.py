"""
Gary Simmons
March 2018
Kata Description: Consider the number triangle below, in which each number is equal to the number above plus the number to the left. If there is no number above, assume the number above is a 0.

1
1 1
1 2 2
1 3 5 5
1 4 9 14 14
The triangle has 5 rows and the sum of the last row is sum([1,4,9,14,14]) = 42.

You will given an integer n and your task will be to return the sum of the last row of a triangle of n-rows.

In the example above:

solve(5) = 42.
More examples in test cases. Good luck!

"""
def solve(n):
    preRow=[1]
    for row in range(0,n-1):
        newRowLen=(len(preRow)+1)
        newRow=[0]*(len(preRow)+1)
        newRow[0]=1
        for x in range(1,newRowLen):
            if x!=(newRowLen-1):
                newRow[x]=preRow[x]+newRow[x-1]
            else:
                newRow[x]=newRow[x-1]
        preRow=newRow
    return sum(newRow)
