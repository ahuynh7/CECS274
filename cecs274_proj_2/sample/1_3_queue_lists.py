class LinkedQueue: 
    #FIFO queue implementation using a singly linked list for storage.
    class Node:
        #Define your node here

    def init(self):
        #Create an empty queue.
        self.head = None
        self.tail = None
        self.size = 0 # number of queue elements

    def len(self):
        #Return the number of elements in the queue.
        return self.size


    def is_empty(self):
        #Return True if the queue is empty.
        return self.size == 0


    def first(self):
        #Return (but do not remove) the element at the front of the queue
        # Youe code here



    def dequeue(self):
        #Remove and return the first element of the queue (i.e., FIFO).
        # Youe code here




    def enqueue(self, e):
        #Add an element to the back of queue
        # Youe code here




    def rotate(self):
        # Youe code here


queue = LinkedQueue()
queue.dequeue() # print error message or throw exception
queue.enqueue(6) # queue = 6
queue.enqueue(2) # queue = 6->2
queue.enqueue(7) # queue = 6->2->7
queue.dequeue() # print 6 and queue = 2->7
queue.first() # print 2 and queue = 2->7
queue.enqueue(1) # queue = 2->7->1
queue.rotate() # queue = 7->1->2
queue.enqueue(5) # queue = 7->1->2->5
