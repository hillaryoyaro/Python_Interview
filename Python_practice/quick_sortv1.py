def quicksort(values):
    if len(values) <= 1:
        return values
    else:
        mid = len(values) //2
        pivot = values[mid]
        left_pivot  = []
        right_pivot = []

        for value in values[1:]:
            if value <= pivot:
                left_pivot.append(value)
            else:
                right_pivot.append(value)
        return quicksort(left_pivot) + [pivot] +quicksort(right_pivot)   

number = [4,78,65,32,90,43,12,4,56]
result = quicksort(number)
print(result)                    