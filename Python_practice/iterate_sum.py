#!/usr/bin/env python3

def sum(numbers):
    """
    Input the list of of numbers and loop over each element and add as total
    Fid output of all element in list.
    Return the total of the sum function.
    Takes O(n)  runtime.
    """
    #Creating a variable total to hold the total sum
    total = 0
    for number in numbers:
        total += number
    return total    
numbers = [55,56,78,44,32,5,99]
result = sum(numbers)
print(result)   