"""
ANH HUYNH
CECS 274
HAILU XU
11/1/20
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # defines a iteration and next function to cycle through the list better
    def __iter__(self):
        self._curr = self

        return self

    def __next__(self):
        if self._curr:       # go next if next is not None
            prev = self._curr       # function needs to remember the prev before shifting the current
            self._curr = self._curr.next

            return prev

        else:
            raise StopIteration

    def __str__(self):
        return self.key + ": " + str(self.value)

class HashTable:
    INIT_CAPACITY = 10

    def __init__(self):
        self._capacity = self.INIT_CAPACITY
        self._size = 0
        self._bucket = [None] * self._capacity

    # prints out the hashtable
    def __str__(self):
        elements = ""

        for i in self._bucket:
            if i == None:
                elements += str(i) + '\n'

            elif isinstance(i, Node):     # if the current bucket element is a node
                elements += ' -> '.join([str(node) for node in iter(i)]) + '\n'

        return elements

    # simple hash function; uses separate chaining for collision handling
    def _simple_hash(self, key):
        hashsum = 0

        # simply splits the key into a list of its char and adds the unicode integer to the hashsum, then the sum is modulated
        for i in [char for char in key]:
            hashsum += ord(i)
            hashsum %= self._capacity

        return hashsum      # fast to compile, but high chance for collisions

    # more complex double hash function; no collisions should occur
    def _double_hash(self, key):
        # placeholder for the highest prime number
        high_prime = 0
        
        # d2(k) = q - k % q
        # largest prime number between 0 and the capacity
        for num in range(0, self._capacity + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break

                else:
                    high_prime = num

        return high_prime - (self._simple_hash(key) % high_prime)

    # utilizes separate chaining collision handling
    def insert(self, key, value):
        ind = self._simple_hash(key)
        new_node = Node(key, value)        
        curr = self._bucket[ind]        # prepares the space of the bucket list to be a node object
        
        if not curr:        # if the bucket index is empty
            self._bucket[ind] = new_node
            self._size += 1

            return      # exits function

        # iterates throught the linked list chain
        while curr.next:
            curr = curr.next

        curr.next = new_node
        self._size += 1

    # utilizes double hasing collision handling
    def add(self, key, value):
        ind = self._simple_hash(key)
        d_ind = self._double_hash(key)
        new_node = Node(key, value)        
        
        if not self._bucket[ind]:        # if the bucket index is empty
            self._bucket[ind] = new_node
            self._size += 1

            return      # exits function

        # if bucket is not empty probe the final key to see if the new index is empty
        new_ind = (ind + d_ind) % self.INIT_CAPACITY
        
        while self._bucket[new_ind]:        # while the the probed index is not empty
            new_ind = (new_ind + d_ind) % self.INIT_CAPACITY

        self._bucket[new_ind] = new_node
        self._size += 1

if __name__ == "__main__":

    # code block for the simple hash function
    simple_hash = HashTable()

    print("HASHTABLE BY SEPARATE CHAINING")
    simple_hash.insert("beta", 2)
    simple_hash.insert("gamma", 4)
    simple_hash.insert("theta", 6)
    simple_hash.insert("tau", 9)
    simple_hash.insert("xi", 25)
    simple_hash.insert("mi", 14)
    simple_hash.insert("phi", 11)
    simple_hash.insert("chi", 5)
    simple_hash.insert("alpha", 3)
    simple_hash.insert("pi", 19)
    print(simple_hash)      # prints separate chained hashtable

    double_hash = HashTable()

    print("HASHTABLE BY DOUBLE HASHING")
    double_hash.add("beta", 2)
    double_hash.add("gamma", 4)
    double_hash.add("theta", 6)
    double_hash.add("tau", 9)
    double_hash.add("xi", 25)
    double_hash.add("mi", 14)
    double_hash.add("phi", 11)
    double_hash.add("chi", 5)
    double_hash.add("alpha", 3)
    double_hash.add("pi", 19)
    print(double_hash)      # prints a completed hashtable