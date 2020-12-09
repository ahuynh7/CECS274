from utils import new_array

from base import BaseList

class ArrayStack(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.a = new_array(1)
        self.n = 0

    def get(self, i):
        # Your code here

    def set(self, i, x):
        # Your code here

    def add(self, i, x): 
        # Your code here

    def remove(self, i): 
        # Your code here
  
    def _resize(self):
        # Your code here


