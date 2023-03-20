import itertools
def kth_permutation(n,k):
    permutations =list(itertools.permutations(range(1,n+1)))
    return ''.join(map(str,permutations[k-1]))

n = 4
k = 16
print(kth_permutation(n,k))    