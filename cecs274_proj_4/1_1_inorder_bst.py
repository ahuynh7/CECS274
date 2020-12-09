class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None      # to identify the parent of a node for deletion

class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._inorder_list = []
        self._size = 0

    # separate insert function for recursion
    def _insert(self, curr, new_node):
        # test left
        if new_node.value < curr.value:
            # test empty
            if not curr.left:
                curr.left = new_node
                new_node.parent = curr

            else:
                self._insert(curr.left, new_node)

        # test right
        elif new_node.value > curr.value:
            # test empty
            if not curr.right:
                curr.right = new_node
                new_node.parent = curr

            else:
                self._insert(curr.right, new_node)

        self._size += 1

    # buffer insert
    def insert(self, value):
        new_node = Node(value)

        if not self._root:
            self._root = new_node
            self._size += 1

        else:
            self._insert(self._root, new_node)
    
    # operates on 3 case
    def delete(self, value):
        del_node = self.find(value)

        # finds the next inorder number after the value of del_node
        def next(value):
            r

        # upon finding the value, if it does not exist, then return none
        if not del_node: return None
        
        # case: 1, if the node has no children
        if not del_node.left and not del_node.right:
            if del_node.value < del_node.parent.value:
                del_node.parent.left = None
            
            else:
                del_node.parent.right = None

        # case: 2, if the node has one child
        elif not del_node.left or not del_node.right:
            if del_node == self._root:      # if the deleted node is the root since the root doesn't have a parent
                if del_node.right:
                    self._root = del_node.right
                    del_node.right = None

                else:
                    self._root = del_node.left
                    del_node.left = None

            elif del_node.left:       # if the left child only exists
                del_node.parent.left = del_node.left

            else:       # if the right child only exists
                del_node.parent.right = del_node.right

        # case: 3, if the node has both children
        else:
            #           inorder_list[(index of value) + 1] gets the next inorder value
            del_value = self._inorder_list[self._inorder_list.index(del_node.value) + 1]
            
            self.delete(del_value)
            del_node.value = del_value

        self._size -= 1

    # recursive
    def _find(self, curr, value):
        if value == curr.value:
            return curr

        elif value < curr.value:
            return self._find(curr.left, value)

        elif value > curr.value:
            return self._find(curr.right, value)
    
    # buffer find
    def find(self, value):
        if not self._root: return None
        else:
            return self._find(self._root, value)

    # buffer function
    def inorder(self):
        self._inorder_list = []

        # checking if nonempty, if not ensue recursion
        if self._root:
            self._inorder(self._root)

        return self._inorder_list

    def _inorder(self, node):
        if not node: return

        self._inorder(node.left)
        self._inorder_list.append(node.value)
        self._inorder(node.right)

    def get_min(self):
        curr = self._root

        while curr.left:
            curr = curr.left

        return curr.value

    def get_max(self):
        curr = self._root
        
        while curr.right:
            curr = curr.right

        return curr.value

    def get_root(self):
        return self._root.value

tree = BinarySearchTree()

# inserting sample numbers
for i in [15, 23, 32, 40, 57, 36, 88]:
    tree.insert(i)

print("min value:", tree.get_min())       # prints minimum: 15
print("max value:", tree.get_max())       # prints maximum: 88
print(tree.inorder())      # prints inorder list
tree.delete(40)     # deleting 40 node
print(tree.inorder())      # prints inorder list
tree.delete(15)     # deleting 15 node
print(tree.inorder())      # prints inorder list
print(tree.get_root())      # prints root of the BST