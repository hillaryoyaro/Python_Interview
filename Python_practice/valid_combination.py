#Given an integer n ,generate all the valid combination 
# of n pairs of parenthesis

#Solution we will use the back trcking techiniqure to solve this
def is_valid(combination):
    stack = []
    for par in combination:
        if par == "(":
            stack.append(par)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack)
x = [2341]
print(is_valid(x))    

