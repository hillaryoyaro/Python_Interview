#! /usr/bin/env python3

def sum(numbers):
    """
    Recursive function to compute the sum of list  ...
    Base case->if list is empty return 0.
    Worse case->.else retun sum . 
    Takes O(n) runtime.
    """
    #base case
    #if not a list does not contain any element.
    if not numbers:
        return 0
    #worse case    
    else: 
        print("Calling sum(%s)"%numbers[1:])   
        remaining_sum = sum(numbers[1:])
        print("Call to sum (%s) returning %d + %d" % (numbers,numbers[0],remaining_sum))
        return numbers[0] + remaining_sum
print(sum([1,2,3,56,78]))    