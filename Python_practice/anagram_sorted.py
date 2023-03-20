#Problem
#Given two strings s1 and S2 ,check if they are anagrams.
#Two strings are anagram if they are made of the same characters with the same frequencies.

def are_anagram(s1,s2):
    """
    base case:if the string are not equal return False,
    else..
    worse case:we sort the string if s1 sorted is equal to s2 sorted we return True
    """
    if len(s1) != len(s2):
        return False

    else:
        return sorted(s1) == sorted(s2)

s1 = "nameless"
s2 = "garden"
print(are_anagram(s1,s2))