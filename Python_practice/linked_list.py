class Node:
    """An object for storing asingle node of a linked list
        Model two attributes- data and next_node,alink to next node of the list
    """
    data = None
    next_node = None

    #creating a constractor ,to initialize the class
    def __init__(self,data):
        self.data = data
    #String interpolation to print out the string
    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data

class LinkedList:
    """Singly linked list.
    """        
    head = None
    #creating a constructor to initialize the attribute
    def __init__(self) -> None:
        self.head = None

     #Create a method to check if the list is empty
    def is_empty(self):
        self.head == None  

    #Create a method that will count the number of Nodes in a list
    def  size(self):
        """Return the number of node in the list Take O(n)time:-wich take a linear time
        """  
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count  

    #Implementation 0f insertion on LinkedList
    def insertion(self,data,index):
        """Insert a new Node containing data at index position
            Insertion takes O(1) ..constant time but finding the node at the 
            insertion point takes O(n) linear time 
            The Operation overllal takes O(n) <linear time>
        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

        while position > 1:
            current = node.next_node
            position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node  

    #Implementation of delete in linked List
    def remove(self,key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current                              


    #Implementation of Append Method in linked_list
    def add(self,data):
        new_node = Node(data)
        #reassign the data to the next node
        new_node.next_node = self.head
        self.head = new_node    

    #Implementation of index of next_node 
    def node_at_index(self,index):
        #Best case scenario
        if index == 0:
            return self.head
        #worst case---> if we don't find the index of node
        else:
            current = self.head
            position = 0

            #while loop to iterate to the next node
            while position < index:
                current = current.next_node
                position += 1
            return current             

    #imprementation of repr inlinked list
    def __repr__(self) -> str:
        """Return a string representation of the list.
           Takes O(n) time which is a linear runtime operation  
        """
        #create empty  list called node and variable of current node and assign it head
        node = []
        current = self.head

        #As long as the current node is not None
        while current:
            #if node assign is same as head,then we append string
            if current is self.head:
                node.append("[Head:%s]" % current.data)
            # if current.next_node is None
            elif current.next_node is None:
                node.append("[Tail:%s]" % current.data)
            # Any Scenario ,which means we are not at tail or head.
            else:
                node.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(node)    

    #Implementation of search in LinkedList
                
    def search(self,key):
        """Search the first Node Containing data that matches the key
       Return the current node if found,else return None if not found
       Takes linear runtimes O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
        #reassign the next node    
            else:
                current = current.next_node    
        return None
