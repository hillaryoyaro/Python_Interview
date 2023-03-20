#problem 
#Given an array of integer arr and an integer k
#Find the kth largest eleement where 1 <= k <= \arr\
#solution using sorting algorith
def kth_largest(arr,k):
    """
    sort the  array using the python inbuild module.such as quick sort.
    Find the length of the list
    return arr[n-k]
    Take O(nlogn) for time complexity
    """
    n = len(arr)
    arr.sort()
    return arr[n-k]
arr = [1,2,3,4,5,6,7,7,9] 
k = 4 
print(kth_largest(arr,k))  