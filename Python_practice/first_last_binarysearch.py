#Problem 2
#Solving the first and last position problem.
#Given asorted array of integers arr and an integer ,target ,find the index of the 
#  first and last position of target i arr
#If target can't be found in arr return [-1,-1]
# 
# Soltion using binary search
def first_last(arr,target):
    #base case:
    if arr[-1] == target:
        return len(arr)-1

    #worse case
    left = 0
    right = len(arr)-1
    #iterate through the arr
    while left <= right:
        mid = (left + right) // 2
        #Iterate the three cases where both conditions are inspected
        if arr[mid] == target and arr[mid + target] > target :
            return mid
         #inspect the second condition if arr is more than target
        elif arr[mid] > target:
            right = mid -1
        #inspect the third condition if arr is less than target
        else:
            left = mid + 1

        return -1              
