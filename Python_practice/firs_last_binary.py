#Problem 2
#Solving the first and last position problem.
#Given asorted array of integers arr and an integer ,target ,find the index of the 
#  first and last position of target i arr
#If target can't be found in arr return [-1,-1]
# 
# Soltion using binary search
def first_last(arr,target):
    #base case
    if arr[0] == target:
        return 0
    #worst case:
    else:
        left = 0
        right = len(arr)-1    
        #iterating through our element.
        while left <= right :
            mid = (left + right) // 2
        #iterating the three cases to check whether the three condition are respected
            if arr[mid] == target and arr[mid-1] < target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    return -1           
arr = [2,4,5,5,5,5,7,9,9]
target = 5
result = first_last(arr,target) 
print(result)