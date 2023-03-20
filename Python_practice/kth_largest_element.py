#problem 
#Given an array of integer arr and an integer k
#Find the kth largest eleement where 1 <= k <= \arr\

def kth_largest(arr,k):
    """
    Repeat k-1 to remove the maximum element.
    Iterate through the element and return maximum arr
    """
    for i in range(k-1):
        
        arr.remove(max(arr))
    return max(arr)

arr = [4,2,9,7,6,7,1,3]
k = 4
result = kth_largest(arr,k)  
print(result)      