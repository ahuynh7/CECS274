"""
ANH HUYNH
CECS 274
HAILU XU
11/1/20
"""

class Node:
    def __init__(self, key: str, value: int, ind=0):
        self.next = None
        self.prev = None
        self.key = key
        self.ind = ind
        self.value = value

    # whenever the object of Node gets printed, this is what is displayed
    def __str__(self):
        return "\"{}\", [{}]: {}".format(self.key, self.ind, self.value)

class DoublyHashMap:
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._size

    def __str__(self):
        elements = ''
        curr = self._head

        while curr:
            elements += (str(curr) + '\n')
            curr = curr.next

        return str(elements)

    # function that shift the index of nodes upon an insertion within the list
    def _reindex(self):
        curr = self._head

        for i in range(self._size):
            curr.ind = i
            curr = curr.next

    def value_at_index(self, ind):
        curr = self._head

        while curr:
            if curr.ind == ind:
                return curr.value     # print entire node

            curr = curr.next

    def value_at_key(self, key):
        curr = self._head

        while curr:
            if curr.key == key:
                return curr.value     # print entire node

            curr = curr.next

    def insert_at_index(self, ind, key, value):
        if ind == 0:
            self.insert_first(key, value)

        elif ind == self._size:
            self.insert_last(key, value)

        else:
            counter = ind
            curr = self._head
            new_node = Node(key, value)

            while counter > 0:
                curr = curr.next
                counter -= 1

            curr.prev.next = new_node
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev = new_node
            self._size += 1

            self._reindex()

    def insert_first(self, key, value):
        # if the lists is empty
        if self._size == 0:
            new_node = Node(key, value)
            self._head = new_node
            self._tail = new_node
            self._size += 1

        else:
            new_node = Node(key, value)
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
            self._size += 1

            self._reindex()

    def insert_last(self, key, value):
        new_node = Node(key, value)
        self._tail.next = new_node
        new_node.prev = self._tail
        self._tail = new_node
        self._size += 1

        self._reindex()

    def remove_at_index(self, ind):
        if self._size == 0:
            raise IndexError
        
        curr = self._head

        while curr:
            # if the curr node is the last on the list
            if not curr.next and curr.ind == ind:
                self._tail = curr.prev
                curr.prev = None
                self._tail.next = None
                self._size -= 1

                return curr.value

            # if the curr node is the first on the list
            elif not curr.prev and curr.ind == ind:
                self._head = curr.next
                curr.next = None
                self._head.prev = None
                self._size -= 1

                self._reindex()

                return curr.value

            # if the curr node is in the middle of the list
            elif curr.ind == ind:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self._size -= 1

                self._reindex()

                return curr.value

            curr = curr.next

    def remove_at_key(self, key):
        if self._size == 0:
            raise IndexError
        
        curr = self._head

        while curr:
            # if the curr node is the last on the list
            if not curr.next and curr.key == key:
                self._tail = curr.prev
                curr.prev = None
                self._tail.next = None
                self._size -= 1

                return curr.value

            # if the curr node is the first on the list
            elif not curr.prev and curr.key == key:
                self._head = curr.next
                curr.next = None
                self._head.prev = None
                self._size -= 1

                self._reindex()

                return curr.value

            # if the curr node is in the middle of the list
            elif curr.key == key:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self._size -= 1

                self._reindex()

                return curr.value

            curr = curr.next

    def remove_at_value(self, value):
        if self._size == 0:
            raise IndexError
        
        curr = self._head

        while curr:
            # if the curr node is the last on the list
            if not curr.next and curr.value == value:
                self._tail = curr.prev
                curr.prev = None
                self._tail.next = None
                self._size -= 1

                return curr.value

            # if the curr node is the first on the list
            elif not curr.prev and curr.value == value:
                self._head = curr.next
                curr.next = None
                self._head.prev = None
                self._size -= 1

                self._reindex()

                return curr.value

            # if the curr node is in the middle of the list
            elif curr.value == value:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self._size -= 1

                self._reindex()

                return curr.value

            curr = curr.next

        else:
            print("ValueError")

m = DoublyHashMap()

m.insert_first("csulb",1)       
m.insert_first("CECS",2)
m.insert_first("CECS274",3)
m.insert_last("CS",4)
m.insert_at_index(1,"life",12)
m.insert_at_index(0,"time",44)
m.insert_at_index(3,"value",12)
m.insert_at_index(4,"good",26)
m.insert_at_index(4,"eng",27)
m.remove_at_value(8)        # no value exist, prints ValueError
m.remove_at_index(1)
m.remove_at_key("time")
m.insert_first("why",24)
m.insert_last("how",57)
m.insert_at_index(3,"know",145)
m.insert_at_index(4,"yes",243)

print("HashTable:\n", end="")
print(m)
print("Length:", len(m))
print("Value at Key 'eng':",m.value_at_key("eng"))
print("Value at Key 'csulb':",m.value_at_key("csulb"))
print("Value at index 3:",m.value_at_index(3))
print("Value at index 7:",m.value_at_index(7))
