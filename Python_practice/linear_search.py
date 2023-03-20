def linear_search(list,target):
    """
    Return the index position of target if found,else return None.
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

#creating a function that verify the index
def verify(index):
    if index is not None: 
        print("Target is found in the list",index)
    else:
        print("Target is not in the list",index)

numbers = [1,2,3,4,5,6,7,8,9]

result = linear_search(numbers,12)
result2 = linear_search(numbers,6)
# Function call
verify(result)
verify(result2)