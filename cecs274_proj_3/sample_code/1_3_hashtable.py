
class Node(object):
    def __init__(self, k, d):
        self.key  = k 
        self.data = d


    
class HashTab(object):
    def __init__(self, size):
        self.__hashArray1 = [None] * (size // 2)  
        self.__hashArray2 = [None] * (size // 2)
        self.__numRecords = 0               
        self.__size = size                  



    def hashFunc(self):
        #Your code here


    def insert(self):
        #Your code here


    def rehash(self, size): #rehash when tables are full
        #Your code here
      
        

    def lookup(self, key):
        #Your code here

  
    def delete(self, key):
        #Your code here



def __main():
    test()
    
if __name__ == '__main__':
    __main()       

def test():
    #Your test case is here, note please put the desired correct outputs of your test case


