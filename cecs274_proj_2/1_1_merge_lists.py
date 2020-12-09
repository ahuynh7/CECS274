"""
ANH HUYNH
CECS 274 
HAILU XU
10/11/20
"""

class Node:
    # contructor funtion that sets needed vars for a node
    def __init__(self, e=None):
        self.e = e
        self.next = None

class LinkedList:
    # constructor which defines a head node
    def __init__(self):
        self.head = Node()
    
    # len() that iterates the list and returns the length
    def __len__(self):
        curr = self.head
        total = 0

        while curr.next!= None:
            total += 1
            curr = curr.next

        return total

    # str() that iterates the list and returns it in a list format
    def __str__(self):
        elements = []
        curr = self.head

        while curr.next != None:
            curr = curr.next
            elements.append(curr.e)

        return str(elements)

    # defines a new node and appends it to the linked list
    def append(self, e):
        new_node = Node(e)
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node
    
    # special function which merges two existing linked list
    def merge(self, list_1, list_2):
        elements = []

        # takes elements of both list and appends it to an element list
        for i in [list_1, list_2]:
            curr = i

            while curr.next != None:
                curr = curr.next
                elements.append(curr.e)

        # iterates through a sorted elements list and appends it to the object's list
        for i in sorted(elements):
            self.append(i)


# Test merge() function
# Linked List of L
L = LinkedList()
L.append(3)
L.append(6)
L.append(9)
L.append(14)
L.append(17)
print("L", L)

# Linked List of M
M = LinkedList()
M.append(2)
M.append(8)
M.append(15)
M.append(19)
M.append(22)
print("M", M)

# Merge Function
LM = LinkedList()
LM.merge(L.head, M.head)
print("LM", LM)