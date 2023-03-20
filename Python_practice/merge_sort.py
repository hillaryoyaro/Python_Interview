
def merge_sort(list):
    """Sort a list in ascending order.
       Return  anew sorted list.
       Divide:Find the midpoint of the list and divide into sublist
       Conqure:Recursive sort the sublist created in previous.
       Combine:Merge the sorted sublist created in previous steps.
    """
    #best case scenario
    if len(list) <= 1:
        return list
    
    left_half,right_half =split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    """Divide unsorted list at midpoint into sublist
       Return two sublit ,left and right 
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left,right 

def merge(left,right):
    """Merge the two list (arrays),sorting them in the process
       Return a new merged list
    """      
    #Declare an empty list l and creating two local variable
    #That keep track of index values that we are going to use to each list
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1

        else:
            l.append(right[j])
            j += 1
    #Incase array is not equal value 
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])

    return l                    

alist = [21,77,17,52,94,68,83,100,20]
l = merge_sort(alist)
print(l)