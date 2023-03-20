def binary_search(list,target):
    """Return the value of index if is midpoint,else return None
    """
    first = 0
    last = len(list)-1
    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1   
    return None             

def verification(index):
    if index is not None:
        print("Index is found in the list",index)
    else:
        print("Inde is not found")

numbers = [1,2,4,5,6,7,8,9,3,10]
#Function call
result =binary_search(numbers,2)
verification(result)       
