# importing to util floor() function
import math

# max heap binary tree imp. 
class MaxHeap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._heap)

    # recursive
    def _floatUp(self, ind1, ind2):     # ind1 = new child index, ind2 = parent node index
        # array value at index
        child = self._heap[ind1 - 1]
        parent = self._heap[ind2 - 1]

        # accounts for unecessary recursion
        if child < parent:
            return

        # swapping action
        self._heap[ind2 - 1] = child     # parent = child
        self._heap[ind1 - 1] = parent       # child = parent

        # if the loop determines that the child is the root, break
        if self.parent(ind2) - 1 != -1:
            self._floatUp(ind2, self.parent(ind2))

    # when deleting
    def _bubbleDown(self, ind):      # ind = parent index
        # accounts for unecessary recursion and if a node only has one child
        try:
            parent = self._heap[ind - 1]
            left = self._heap[self.left(ind) - 1]
            right = self._heap[self.right(ind) - 1]

        except IndexError:
            return

        # go to left child if it is greater
        if left > right:
            self._heap[ind - 1] = left
            self._heap[self.left(ind) - 1] = parent

            self._bubbleDown(self.left(ind))
        
        # go to right child if it is greater
        elif right > left:
            self._heap[ind - 1] = right
            self._heap[self.right(ind) - 1] = parent

            self._bubbleDown(self.right(ind))

    def parent(self, ind):
        return math.floor(ind / 2)

    def left(self, ind):
        return ind * 2

    def right(self, ind):
        return ind * 2 + 1

    def push(self, e):
        self._heap.append(e)
        self._size += 1

        # tests if the new element is larger than its parent to it could be floated up
        if self._size == 0:
            return      # do nothing

        elif e > self._heap[self.parent(self._size) - 1]:
            self._floatUp(self._size, self.parent(self._size))

    def pop(self):
        max_value = self._heap[0]       # records the greatest value

        # swapping the last with the first in the heap array
        self._heap[0] = self._heap[-1]
        self._heap[-1] = max_value
        self._heap.pop()        # removes last value
        self._size -= 1

        self._bubbleDown(1)

        return max_value

pqueue = MaxHeap()
pqueue.push(22)
pqueue.push(31)
pqueue.push(12)
pqueue.push(46)
pqueue.push(37)
pqueue.push(32)
print(pqueue)
pqueue.pop()
print(pqueue)
pqueue.pop()
pqueue.push(66)
pqueue.push(42)
pqueue.push(56)
print(pqueue)
pqueue.pop()
pqueue.push(41)
pqueue.push(121)
print(pqueue)
pqueue.pop()
print(pqueue)

# Default outputs:
#[46, 37, 32, 22, 31, 12]
#[37, 31, 32, 22, 12]
#[66, 32, 56, 22, 31, 12, 42]
#[121, 56, 42, 32, 31, 12, 41, 22]
#[56, 32, 42, 22, 31, 12, 41]
