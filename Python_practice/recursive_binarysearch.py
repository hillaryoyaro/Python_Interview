def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint= (len(list)) // 2 
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target)
            else:          
                return recursive_binary_search(list[:midpoint],target)

def verification(index):
    if index is not None:
        print("The index is found",index)
    else:
        print("The index is not found")                    
                
number = [1,2,3,4,5,6,7,8,9,10]
#Function call                
result = recursive_binary_search(number,7)
verification(result)
