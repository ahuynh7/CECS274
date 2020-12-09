
class priorityQueue:
    def __init__(self):
        self.heap=[]                # an array of integers
        self.size = 0               # the size of heap

    def __len__(self):
        return self.size

    def parent(self,index):
        #Your code here
        
    def leftChild(self,index):
        #Your code here
        
    def rightChild(self,index):
        #Your code here
        
    def swap(self, index1, index2):
        #Your code here
        
    def insert(self,x):
        #Your code here


    def delete_Max(self):
        #Your code here

       

#Test case
h = priorityQueue()
h.insert(22)
h.insert(31)
h.insert(12)
h.insert(46)
h.insert(37)
h.insert(32)
print(h.heap)
x = h.delete_Max()
print(h.heap)
x = h.delete_Max()
h.insert(66)
h.insert(42)
h.insert(56)
print(h.heap)
x = h.delete_Max()
h.insert(41)
h.insert(121)
print(h.heap)
x = h.delete_Max()
print(h.heap)
# Default outputs:
#[46, 37, 32, 22, 31, 12]
#[37, 31, 32, 22, 12]
#[66, 32, 56, 22, 31, 12, 42]
#[121, 56, 41, 32, 31, 42, 12, 22]
#[56, 32, 41, 22, 31, 42, 12]