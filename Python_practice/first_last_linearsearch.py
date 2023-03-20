#Problem 2
#Solving the first and last position problem.
#Given asorted array of integers arr and an integer ,target ,find the index of the 
#  first and last position of target i arr
#If target can't be found in arr return [-1,-1]
# 
# Soltion using Linear search
def first_last(arr,target):
    """
    base case:-iterate throught the array ,if arr is equal to target start and i
    worst case:- if target is not found return [-1,-1]
    """  
    for i in range(len(arr)):
        if arr[i] == target:
            #initialize variable start with i
            start = i
            #iterage through the index to find the next target
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start,i]

    return [-1,-1]   

arr = [2,4,5,5,5,5,7,9,9]
target = 5
result = first_last(arr,target)
print(result)         