#Given a binary tree roo.Check if its symmetric a round its center
#(Amirror of itself)
#A symmetric :is defined as balanced and propotion 
# similarity that found in two halves of an object

# solution we will use the depth first search algorith
def are_symmetric(root1,root2):
    #First case:Both don't exist no root1 and root2 respectively.
    #return True
    if root1 is None and root2 is None:
        return True
    #second case:One of them exist but the other one doesn't
    # return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return True
    #Third case:if they have different root values
    # return False
    else:
        return are_symmetric(root1.left,root2.right) and are_symmetric(root1.right,root2.left) 
def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left,root.right)    


node1 = [5,2,8,9,7,1,3,0,6]
node2 = [5,2,8,9,7,1,3,0,6]
result = are_symmetric(node1,node2)
print(result)
              