
class Entry:
    def __init__(self,key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self,numBuckets):
        # Your code here
    
    def simple_hash(self,key):
        # Your code here, note you should discuss the design of your simple hash function

    def double_hash(self,key):
        # Your code here, note you should discuss the design of your double hash function
    
    def add(self,key,value):
        # Your code here, note when use simple hash, use separate chaining to handle collisions
    
    def updateValue(self,key,value):
        # Your code here
    
    def delete(self,key):
        # Your code here
    
    def lookUp(self,key):
        # Your code here
        
    def print(self):
        # Your code here
    
if __name__ == '__main__':
    
    ht = HashTable(100)

    # define your own test cases
    # It should display the outputs with two types of hashing

    print(ht)
