class Node:
    """
        Creating a node with two attributes data and next,
        next is a reference ,which point to the next node. 
    """
    data = None
    next = None
    def __init__(self,data) -> None:
        """Initialize the attribute with self
        """
        self.data = data 
        self.next = None

class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_head(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head =new_node 

    def search(self,x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            #increament the search value from first to last 
            # reassign the value
            temp = temp.next 
             
        else:
            return False 

    def delete_node(self,data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
            prev.next = temp.next  

    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None                              
#Creating an instance of family
family = LinkedList()
family.head = Node("Hillary")
wife = Node("Wintana") 
first_kid = Node("Lisa")
second_kid = Node("Bob")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid
family.insert_new_head("Davy")
family.traversal()
result = family.search("Mike")
futa = family.delete_node("Bob")
print(futa)
print(family.delete_tail())


