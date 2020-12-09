from utils import new_array


class DynamicArray:

    def __init__(self):
        self.a = new_array(1)
        self.n = 0
        self.capacity = len(self.a)

    def resize(self, capacity):
        b = new_array(capacity)
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b
        self.capacity = capacity

    def insert(self, k, value):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)

        for j in range(self.n, k, -1):
            self.a[j] = self.a[j-1]
        self.a[k] = value
        self.n += 1

    def __str__(self):
        s = "["
        for i in range(self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        s += "]"
        return s


dynamic_array = DynamicArray()

dynamic_array.insert(0, 2)
dynamic_array.insert(0, 1)
dynamic_array.insert(0, 3)
dynamic_array.insert(1, 4)

print(dynamic_array)
