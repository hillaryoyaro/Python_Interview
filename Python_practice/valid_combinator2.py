#Given an integer n ,generate all the valid combination 
# of n pairs of parenthesis

#Solution we will use the back trcking techiniqure to solve this
def is_valid(combinator):
    diff = 0
    for par in combinator:
        if par == "(":
            diff += 1
        else:
            if diff == 0:
                diff += 1
            else:
                diff -= 1
    return diff == 0                    