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

class CircularLinkedList:
    # constructor which defines a head node
    def __init__(self):
        self._head = Node()
        self._size = 0
    
    # len() that iterates the list and returns the length
    def __len__(self):
        return self._size

    # str() that iterates the list and returns it in a list format
    def __str__(self):
        elements = []
        curr = self._head

        while curr.next != self._head.next or len(elements) == 0:
            curr = curr.next
            elements.append(curr.e)    

        return str(elements)

    # defines a new node and appends it to the linked list
    def append(self, e):
        # if the list is empty, have the head node point to the new node and have the new node point to what the head node is pointing to (itself)
        if self._size == 0:
            new_node = Node(e)
            self._head.next = new_node
            new_node.next = self._head.next
            self._size += 1

        # else, loop to the last node and have it point to the new node and the new node to point to the head node.next
        else:
            new_node = Node(e)
            curr = self._head.next

            while curr.next != self._head.next:
                curr = curr.next

            curr.next = new_node
            new_node.next = self._head.next
            self._size += 1

# testing the circular linked list
l = CircularLinkedList()
l.append(4)
l.append(5)
l.append(7)
l.append(8)
l.append(12)
l.append(56)
l.append(85)
l.append(41)
print(l)        # prints the list
print("The count number is",  len(l))      # obtains the length