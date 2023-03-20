def are_anagram(s1,s2):
    """
    Comparing the two string s1 and s2 if are anagram
    if s1 == s2 return True
    Base case:-if s1 is not equal to s2 return False,else
    Worse case:-perform recursive operation and return True if s1 == s2
    Takes time complexity O(n) time
    Space complexity of  S(n) = O(n) space
    """
    if len(s1) != len(s2):
        return False
    #Worse case
    else:
        #create an hash table
        freq1 = {}
        freq2 = {}

        #Traversing in s1
        for ch in s1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1

        for ch in s2:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1   
    for key in freq1:
        if key not in freq2 or freq2[key] != freq2[key]:
            return False
    return True

s1 = "danger"
s2 = "garden"
result = are_anagram(s1,s2)
print(result)                       
