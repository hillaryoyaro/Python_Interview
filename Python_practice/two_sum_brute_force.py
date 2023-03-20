#Given an array of integers arr and an integer and an integer k
#Find the indices of two elements that sum up to k

# Solution
#The function will be: sum_of_two
#the parameter will be array of arr and integer of k
#solve using brute force algorith

def sum_of_two(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == k:
                return [i + j]
    return [-1,-1]            