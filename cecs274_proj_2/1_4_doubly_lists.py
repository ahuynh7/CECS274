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
        self.prev = None        # necessary for the doubly linked list

# doubly linked list implementation 
# **THIS LIST DOES NOT ACCOUNT FOR INDEX ERRORS WHEN CALLING UPON FUNCTIONS**
# // simply because it is not required in the project rubrick
class DoublyLinkedList:
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

        while curr.next != None:
            curr = curr.next
            elements.append(curr.e)

        return str(elements)

    # return a boolean if the list is empty
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    # returns a boolean if the list is a palindrome: same forwards and backwards
    def is_palindrome(self):
        elements_fw = []
        elements_bw = []
        curr = self._head

        # counting forwards
        while curr.next != None:
            curr = curr.next
            elements_fw.append(curr.e)
        
        elements_bw.append(curr.e)

        # counting backwards; while the current node is not what the head node points to
        while self._head.next != curr:
            curr = curr.prev
            elements_bw.append(curr.e)

        if elements_fw == elements_bw:
            return True

        else:
            return False

    # gets the element of a node at a certain index
    def get(self, ind):
        curr = self._head
        counter = ind

        while counter >= 0:
            curr = curr.next
            counter -= 1

        return curr.e

    # sets a new value to a node at a certain index
    def set(self, ind, e):
        curr = self._head
        counter = ind

        while counter >= 0:
            curr = curr.next
            counter -= 1

        curr.e = e

    # adds an element at a certain index
    def add(self, ind, e):
        # we assume the user will always input non erroneous indices 
        if self.is_empty() and ind == 0:        # if the list is empty and the index is 0
            new_node = Node(e)
            self._head.next = new_node
            self._size += 1

        else:
            new_node = Node(e)
            curr = self._head
            counter = ind

            # to account for the index
            while counter > 0:
                curr = curr.next
                counter -= 1

            if curr.next == None:
                self.append(e)

            else:
                new_node.next = curr.next
                curr.next.prev = new_node
                curr.next = new_node
                new_node.prev = curr
                self._size += 1

    def append(self, e):
        new_node = Node(e)
        curr = self._head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr
        self._size += 1

    # removes at a certain index, assuming the user will not input erroneous indices
    def remove(self, ind):
        if self.is_empty():
            print("IndexError")

        else:
            curr = self._head
            counter = ind

            # to account for the index
            while counter >= 0:
                curr = curr.next
                counter -= 1

            if curr.next == None:
                curr.prev.next = None
                curr.prev = None
                self._size -= 1

            else:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self._size -= 1

            return curr.e

dl = DoublyLinkedList()
dl.remove(0)    # print error message or raise exception
dl.add(0,5)
print(dl)   # print [5]
dl.add(0,1)
print(dl)   # print [1,5]
dl.add(1,3)
print(dl)   # print [1,3,5]
dl.add(2,6)
print(dl)   # print [1,3,6,5]
dl.remove(2)
print(dl)   # print [1,3,5]
dl.add(1,2)
print(dl)   # print [1,2,3,5]
dl.add(3,4)
print(dl)   # print [1,2,3,4,5]
dl.append(6)
print(dl)   # print [1,2,3,4,5,6]
dl.set(5,1)
print(dl)   # print [1,2,3,4,5,1]
dl.remove(3)
print(dl)   # print [1,2,3,5,1]
print(dl.is_palindrome())    # print False
dl.set(1,5)
print(dl)   # print [1,5,3,5,1]
print(dl.is_palindrome())    # print True
