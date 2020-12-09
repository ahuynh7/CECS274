"""
ANH HUYNH
CECS 274 
HAILU XU
9/28/20
"""

import ctypes

class QueueArray:
    # init variables
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.Array = self._make_array(self.capacity)

    # returns length of array
    def __len__(self):
        return self.n

    # prints the array to be easily digestable
    def __str__(self):
        return(str([self.Array[i] for i in range(self.n)]))

    # resizes a new array with pre-implemented value
    def _resize(self, new_capacity, *ins_ind):
        temp_array = self._make_array(new_capacity)

        for i in range(self.n):
            temp_array[i] = self.Array[i]       # for loops to copy all data to new array

        self.Array = temp_array
        self.capacity = new_capacity

    # creates a list based on the ctypes imported class
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def get_item(self, ind):
        return self.Array[ind]

    # appending an element based on index n
    def add(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)      # if resize occurs, the capacity is doubled

        self.Array[self.n] = element
        self.n += 1

    # FIFO, so the head element is removed
    def remove(self):
        if self.n == 0:
            print("Queue is empty")
        else:
            dequeue = self.Array[0]       # temporarily stores the dequeue value

            for i in range(self.n - 1):
                self.Array[i] = self.Array[i + 1]

            self.n -= 1

            return dequeue

# testing the array queue
queue = QueueArray()

queue.remove() # it prints “Queue is empty”
queue.add(1)
queue.add(2)
queue.add(3)
queue.remove() # it returns 1
queue.add(4)
queue.remove() # it returns 2
queue.remove() # it returns 3
queue.add(5)
queue.remove() # it returns 4
queue.remove() # it returns 5
queue.remove() # it prints “Queue is empty”