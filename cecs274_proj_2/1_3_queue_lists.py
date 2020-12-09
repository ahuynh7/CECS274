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

# implements a FIFO queue list
class QueueLinkedList:
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

        while curr.next != None:
            curr = curr.next
            elements.append(curr.e)    

        return str(elements)

    # return if the list is empty
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    # return (but do not remove) the element at the front of the queue
    def first(self):
        return self._head.next.e

    # defines a new node and queue it to the front of the linked list
    def enqueue(self, e):
        new_node = Node(e)
        curr = self._head
        
        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            print("IndexError")

        else:
            curr = self._head.next
            self._head.next = curr.next
            self._size -= 1

            return curr.e

    def rotate(self):
        if self.is_empty():
            print("IndexError")

        else:
            self.enqueue(self.dequeue())

queue = QueueLinkedList()

queue.dequeue() # print error message or throw exception
print(queue)
queue.enqueue(6) # queue = 6
print(queue)
queue.enqueue(2) # queue = 6->2
print(queue)
queue.enqueue(7) # queue = 6->2->7
print(queue)
print(queue.dequeue()) # print 6 and queue = 2->7
print(queue)
print(queue.first()) # print 2 and queue = 2->7
print(queue)
queue.enqueue(1) # queue = 2->7->1
print(queue)
queue.rotate() # queue = 7->1->2
print(queue)
queue.enqueue(5) # queue = 7->1->2->5
print(queue)
