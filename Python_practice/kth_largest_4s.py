#problem 
#Given an array of integer arr and an integer k
#Find the kth largest eleement where 1 <= k <= \arr\
#solution using heap algorith
import heapq
def kth_largest(arr,k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range (k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)


number = [4,2,9,7,6,7,1,3] 
k = 4 
print(kth_largest(number,k))      