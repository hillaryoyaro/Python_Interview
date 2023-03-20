#Problem
#Given two strings s1 and S2 ,check if they are anagrams.
#Two strings are anagram if they are made of the same characters with the same frequencies.


#Using counter collectio module to solve the probrem rather than using hash tables
#we will import class Counter from collection module

from collections import Counter
def are_anagrams(s1,s2):
    """
    base case :- if len(s1) is not equal to len(s2) return False.
    worse case :- if counter(s1) is equal to counter (s2) return the statement. 
    """
    if len(s1) != len(s2):
        return False
    else:
        return Counter(s1) == Counter(s2)
s1 = "nameless"
s2 = "salesmen"
print(are_anagrams(s1,s2))        
