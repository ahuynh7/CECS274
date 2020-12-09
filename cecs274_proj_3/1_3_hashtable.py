"""
ANH HUYNH
CECS 274
HAILU XU
11/1/20

IMCOMPLETE CODE; PROMPT WAS HARD TO UNDERSTAND
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return self.key + ": " + str(self.value)

class HashTable:
    INIT_CAPACITY = 4

    def __init__(self):
        self._capacity = self.INIT_CAPACITY // 2
        self._size = 0
        self._bucket_one = [None] * self._capacity
        self._bucket_two = [None] * self._capacity

    def __str__(self):
        elements = ""

        for i in self._bucket_one:
            elements += str(i) + '\n'
        
        elements += '\n'

        for i in self._bucket_two:
            elements += str(i) + '\n'

        return elements 

    # hash function for first bucket array; collisions are common
    def _hash_one(self, key):
        hashsum = 0

        # simply splits the key into a list of its char and adds the unicode integer to the hashsum, then the sum is modulated
        for i in [char for char in key]:
            hashsum += ord(i)
            hashsum %= self._capacity

        return hashsum      # fast to compile, but high chance for collisions

    # more complex hash function for second bucket array; no collisions should occur
    def _hash_two(self, key):
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

        return high_prime - (self._hash_one(key) % high_prime)

    # utilizes separate chaining collision handling
    def insert(self, key, value):
        ind_one = self._hash_one(key)
        new_node = Node(key, value)
        curr = self._bucket_one[ind_one]
        
        # simple: if either table slots are empty
        if not curr:
            self._bucket_one[ind_one] = new_node

        elif not self._bucket_two[(self._hash_two(curr.key) + ind_one) % self._capacity]:       # if the second table is not empty
            self._bucket_two[(self._hash_two(curr.key) + ind_one) % self._capacity] = curr
            self._bucket_one[ind_one] = new_node

        while curr:
            if curr in self._bucket_one:
                curr = self._bucket_two[(self._hash_two(curr.key) + ind_one) % self._capacity]

            elif curr in self._bucket_two:
                pass

        self._size += 1

    def delete(self, key):
        pass

    def search(self, key):
        pass

ht = HashTable()
ht.insert("trea", 1)
ht.insert("cick", 2)
#ht.insert("refe", 3)
print(ht)