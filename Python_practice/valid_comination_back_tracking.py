def generate(n):
    def rec(n,diff,comb,combs):
        #base case
        if diff < 0:
            return 
        #base cse 
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb)) 
        #worse case:
        else:
            comb.append('(')
            rec(n-1,diff+1,comb,combs)
            comb.pop()
            comb.append(')')
            rec(n-1,diff-1,comb,combs)
            comb.pop()
        comb = []
        rec(2 * n,0,[],combs)
        return combs

x = 9
print(generate(x))        