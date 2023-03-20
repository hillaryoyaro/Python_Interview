def binary_search(list,target):
    first = 0
    last = len(list)-1
    
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1

# verify the function
def verify(index):
    if index is not None:
        print("The target is in the list",index)
    else:
        print("The target is not in the list",index)

#create the list argument
numbers = [1,2,3,4,5,6,7,8,9]
#passing the argument to the function defination
result = binary_search(numbers,6)
#Function call
verify(result)            