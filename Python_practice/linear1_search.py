def linear_search(list,target):
    """Return the index position of target if found,else return None
    """
    for i in range(len(list)):
        if list[i] == target:
            return i
        
    return None

def verify(index):
    """
    Print the index if not None ,else not found
    """  
    if index  is not None:
        print("Index is found ",index) 
    else:
        print("Index not found")
# Function call
number = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(number,12)
verify(result)      

result = linear_search(number,6)
verify(result) 