def quicksort(values):
    if len(values) <= 1:
        return values
    else:
        pivot = values[len(values) // 2] 
        left_pivot = []
        right_pivot = []

        for value in values:
            if value <= pivot:
                left_pivot.append(value)
            else:
                right_pivot.append(value)
        return quicksort(left_pivot) + [pivot] +quicksort(right_pivot) 
numbers = [89,90,6,56,77,42,78]
print(quicksort(numbers))                      