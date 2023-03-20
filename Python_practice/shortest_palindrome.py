def shortest_palindrome(string):
    for i in range(len(string)):
        if string[:i+1] == string[:i+1][::-1]:
            return string[i+1:][::-1] + string
    return string[::-1] + string

x = "Hillary"
result = shortest_palindrome(x)
print(result)            
