def quick_sort(values):
    """
    sort the array 
    base case:if len(arr) is equal to zero return 0
    worse case:perform recrsive call
    """
    if len(values) <= 1:
        return values
    #worse case:
    else:
        pivot = [0]
        left_pivot = []
        right_pivot = []

        for value in values[1:]:
            if value <= pivot:
                left_pivot.append(value)
            
            else:
                right_pivot.append(value)  
        return quick_sort(left_pivot) + [pivot] + quick_sort(right_pivot)
                     

numbers = [4,2,9,7,6,7,1,3]   
print(quick_sort(numbers))     