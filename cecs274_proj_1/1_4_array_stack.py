"""
ANH HUYNH
CECS 274 
HAILU XU
9/28/20
"""

import ctypes

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

    def get(self, ind):
        return self.Array[ind]

    # appending an element based on index n
    def push(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)      # if resize occurs, the capacity is doubled; this ensures an amortizes update time of O(1)

        self.Array[self.n] = element
        self.n += 1

    # removes the last item LIFO
    def pop(self):
        destack = self.Array[self.n - 1]       # temporarily stores the dequeue value
        temp_array = self._make_array(self.capacity)

        for i in range(self.n - 1):
            temp_array[i] = self.Array[i]

        self.Array = temp_array
        self.n -= 1

        return destack

    def add(self, ind, value):
       if self.n == self.capacity:
           self._resize(2 * self.capacity)
       
       # instead of shifting elements via loop, shift elements by indexing blocks and concatenating it to a temporary array
       temp_array = self.Array[0: ind] + [value] + self.Array[ind: self.n]
       self.Array = temp_array
       self.n += 1

# tests the code
stack = StackArray()

stack.add(0,1)
stack.add(0,2)
stack.add(1,3)
stack.add(3,5)
stack.add(2,4)
print(stack.get(0)) # it prints 2
print(stack.get(1)) # it prints 3
print(stack.get(2)) # it prints 4
print(stack.get(3)) # it prints 1
print(stack.get(4)) # it prints 5