"""
ANH HUYNH
CECS 274 
HAILU XU
9/28/20
"""

# LINE 52 SHOWS THAT THE PARAMETERS MULTIPLIES THE NEW CAPACITY BY 2

import ctypes

# stack class
class StackArray:
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
            temp_array[i] = self.Array[i]

        self.Array = temp_array
        self.capacity = new_capacity

    # creates a list based on the ctypes imported class
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    # determines whether the stack is empty or not and returns it
    def is_empty(self):
        if self.n == 0:
            return True
        else:
            return False

    # appending an element based on index n
    def push(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)      # if resize occurs, the capacity is doubled; this ensures an amortizes update time of O(1)

        self.Array[self.n] = element
        self.n += 1

    # dequeues the last item LIFO
    def pop(self):
        destack = self.Array[self.n - 1]       # temporarily stores the dequeue value
        temp_array = self._make_array(self.capacity)

        for i in range(self.n - 1):
            temp_array[i] = self.Array[i]

        self.Array = temp_array
        self.n -= 1

        return destack

class Queue():
    def __init__(self):
        # initializes two stacks, so that the queue FIFO property can be imitated
        self._stack_one = StackArray()
        self._stack_two = StackArray()

    def __str__(self):
        return(str(self._stack_one) + '\n' + str(self._stack_two))

    # queue function
    def queue(self, e):
        self._stack_one.push(e)

    # dequeue function
    def dequeue(self):
        # if both queues are empty, then print empty
        if self._stack_one.is_empty() and self._stack_two.is_empty():
            print("Queue is empty")

        # when stack one has accumulated and stack two is empty
        elif not self._stack_one.is_empty() and self._stack_two.is_empty():
            # transfers all values from the first stack to the second one to be "dequeued"
            while not self._stack_one.is_empty():
                self._stack_two.push(self._stack_one.pop())

            dequeue = self._stack_two.pop()     # stores the value for the "dequeue" value

            # transfers all values from the second stack to the first stack to be "queued"
            while not self._stack_two.is_empty():
                self._stack_one.push(self._stack_two.pop())

            return dequeue

# test the code
queue = Queue()

queue.dequeue() # it prints “Queue is empty”
queue.queue(1)
queue.queue(2)
queue.queue(3)
queue.dequeue() # it returns 1
queue.queue(4)
queue.dequeue() # it returns 2
queue.dequeue() # it returns 3
queue.queue(5)
queue.dequeue() # it returns 4
queue.dequeue() # it returns 5
queue.dequeue() # it prints “Queue is empty”
