from linked_list import LinkedList
def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list

    Takes O(n log n) time
    Takes O(n) space
    """
    #Determine the best case of the linked_list
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        #Meaning its empty list
        return linked_list
    else:
        #Splitting the list into left_half and right_half the traverse the list
        #We will implement by helper methods to make this easier
        left_half, right_half = split(linked_list)
        left = merge_sort(left_half)
        right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(log n) time
    """
    #Best Case scenario.
    if linked_list == None or linked_list.head == None:
        # Incase linkedlist contains a single node and empty
        # we are Going to assign the entire list with left_half variable to linked_list
        # And right_half with None
        # Return left_half and right_half
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        #Worst case scenario.
        #Start by finding the size of linked_list.
        size = linked_list.size()
        mid = size // 2
        #Finding the mid_node of the linked list
        mid_node = linked_list.node_at_index(mid-1)

        #Reassign our variable after loosing the connection
        #Find distinct linked_list 
        left_half = linked_list
        #Right_half will create a new instance
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    Takes O(n) space
    Runs in O(n) time
    """

    # Create a new linked list that contains nodes from merging left and right
    #Creating an instance.
    
    merged = LinkedList()
    # Add a fake head(pointer) that is discarded later.
    merged.add(0)
    #set current to the head of  the linked list(The pointer that point to the addresss of the first head)
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right as long until the tail node of both
    # left and right
    while left_head or right_head:
        # If the head node of left is None, we're at the tail
        # Add the tail node from right to the merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            #(This is basically a stopping condition).
            right_head = right_head.next_node 
        # If the head node of right is None, we're at the tail
        # Add the tail node from left to the merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            #(This is basically a stopping condition).
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            # If data on left is lesser than right set current to left node
            # Move left head to next node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # If data on left is greater than right set current to right node
            # Move right head to next node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(15)
l.add(25)
l.add(70)
l.add(200)
l.add(450)
print(l)    
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)