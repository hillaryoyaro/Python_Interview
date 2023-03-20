def smallest_missing_positive_integer(A):
    # Filter out negative numbers and duplicates
    A = set([x for x in A if x > 0])

    # If A is empty, return 1
    if not A:
        return 1

    # Sort A
    A = sorted(A)

    # Iterate through A to find smallest missing positive integer
    smallest = 1
    for i in range(len(A)):
        if A[i] == smallest:
            smallest += 1
        elif A[i] > smallest:
            return smallest

    # If all numbers in A are consecutive, return the next integer
    return smallest

number = [1,2,3,1,4,6]
print(smallest_missing_positive_integer(number))   
