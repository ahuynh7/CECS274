
class Node:
  def __init__(self, key=None):
    self.key = key
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None


  def findMin_ini(self):
    FNode = self.findMin(self.root)
    return FNode
  
  def findMax_ini(self):
    FNode = self.findMax(self.root)
    return FNode

  def traverseInOrder_ini(self):
    self.traverseInOrder(self.root)



  def findMin(self, root):
   #Your code here




  def findMax(self, root):
    #Your code here



  def insertInTree(self, root, key):
    #Your code here



  def delete(self, root, key):
    #Your code here



  def traverseInOrder(self, root):
    #Your code here


  def delete_ini(self, key):
    self.root = self.delete(self.root, key)

  def insert(self, data):
    self.root = self.insertInTree(self.root, data)

  def visit(self, node):
    print (node.key)

  def getRoot(self):
    return self.root


def main():

  print ("\nInsert the following numbers: ")
  print ("15, 23, 32, 40, 57, 36, 88")

  Tree = BST()
  Tree.insert(15)
  Tree.insert(23)
  Tree.insert(32)
  Tree.insert(40)
  Tree.insert(57)
  Tree.insert(36)
  Tree.insert(88)

  print ("Output the Min Value: ")
  min = Tree.findMin_ini()
  print (min.key, "\n")

  print ("Output the Max Value: ")
  max = Tree.findMax_ini()
  print (max.key, "\n")

  print ("Inorder traversal of the given tree: ")
  Tree.traverseInOrder_ini()

  print ("\n Now delete 40")
  Tree.delete_ini(40)

  print ("\nInorder traversal of tree")
  Tree.traverseInOrder_ini()

  print ("\n Now delete 15")
  Tree.delete_ini(15)

  print ("\nInorder traversal of tree")
  Tree.traverseInOrder_ini()

  print ("\nOutput the new root node: ")
  gt = Tree.getRoot()
  print (gt.key)

 
if __name__ == "__main__":
  main()

