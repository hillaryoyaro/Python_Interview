def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index + 1]:
            return False
    return True
def validate(index):
    if index is not None:
        print("presence i the list",index)
    else:
        print("not presense")


number = [34,83,56,88,77,99,101]
result = is_sorted(number)
validate(result)                        