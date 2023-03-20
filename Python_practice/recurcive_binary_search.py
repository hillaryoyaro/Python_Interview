def recursive_binary_search(list,target):
    #what happen if empty list is passed we return false.
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:],target)
            else:
                return recursive_binary_search(list[:midpoint -1],target)
                
def verify(result):
    if result is not None:
        print("The number is in the list:",result)
    else:
        print("The number is not in the list:",result)
numbers = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers,12) 
#function call
verify(result)           