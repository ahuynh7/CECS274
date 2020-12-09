"""
ANH HUYNH
CECS 274 
HAILU XU
9/28/20
"""

import ctypes

class DynamicArray:
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
        temp_array = self._make_array(new_capacity)     # make a new array double-sized

        # replicating all values to the new array.
        for i in range(self.n):
            temp_array[i] = self.Array[i]

        self.Array = temp_array
        self.capacity = new_capacity

    # creates an array based on the ctypes imported class
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def get_item(self, ind):
        return self.Array[ind]

    # appending an element based on index n
    def append(self, element):
        self.Array[self.n] = element
        self.n += 1

   # inserting an element at a certain index
    def insert(self, ind, value):
       if self.n == self.capacity:
           self._resize(2 * self.capacity)
       
       # instead of shifting elements via loop, shift elements by indexing blocks and concatenating it to a temporary array
       temp_array = self.Array[0: ind] + [value] + self.Array[ind: self.n]
       self.Array = temp_array
       self.n += 1


# calls the class
dynamic_array = DynamicArray()

dynamic_array.insert(0,1)
dynamic_array.insert(0,2)
dynamic_array.insert(1,3)
dynamic_array.insert(3,5)
dynamic_array.insert(2,4)
print(dynamic_array) # it prints [2,3,4,1,5]