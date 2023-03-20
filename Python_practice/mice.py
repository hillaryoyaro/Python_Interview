#Return minimum time required to place mice in holes using the Greedy Approach.
#We can put every mouse to its nearest hole to minimize the time complexity.
#This can be done by srting the position of mice and holes.

def assignHoles(mice,holes):
    #Base -num of mice and holes should be the same.
    if len(mice) != len(holes):
        return "Number of mice and holes not the same"

    #sort first
    mice.sort()
    holes.sort()

    #Finding maax ddifference between 1 th mice and holes
    max_diff = 0
    for i in range(len(mice)):
        if max_diff < abs(mice[i] - holes[i]):
            max_diff = abs(mice[i]-holes[i])
        return max_diff

mice = [4,-4,2]
holes = [4,0,5]        
result = assignHoles(mice,holes)
print(result)