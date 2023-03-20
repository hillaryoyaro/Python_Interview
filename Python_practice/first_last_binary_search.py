#Problem 2
#Solving the first and last position problem.
#Given asorted array of integers arr and an integer ,target ,find the index of the 
#  first and last position of target i arr
#If target can't be found in arr return [-1,-1]
# 
# Soltion using binary search
def first_and_last(arr,target):
    #base case
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1,-1]

    #worst case
    start = first_and_last(arr,target)
    end = first_and_last(arr,target)
    return [start,end]    

arr = [2,4,5,5,5,5,7,9,9]
target = 5
result = first_and_last(arr,target) 