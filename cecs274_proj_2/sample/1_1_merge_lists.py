class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next


class LinkedList:
  def __init__(self):  
    self.head = None
  

  def insert(self, data):
    #Your code here



  def printLL(self):
    #Your code here




def merge(List_1, List_2) -> Node:
    #Your code here



# Test merge() function
# Linked List of L
L = LinkedList()
L.insert(3)
L.insert(6)
L.insert(9)
L.insert(14)
L.insert(17)
# Linked List of M
M = LinkedList()
M.insert(2)
M.insert(8)
M.insert(15)
M.insert(19)
M.insert(22)
# Merge Function
LM = LinkedList()
LM.head = merge(L.head, M.head)
LM.printLL()
