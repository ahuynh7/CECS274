class Node:
    def __init__(self,key,val):
        self.value = val
        self.next = None
        self.prev = None
        self.key = key
        self.index = 0
        
class HashTable:
    def __init__(self):
        self.head = None
        self.tail = None
                  
    def insert_by_Index(self,index,key,val):
       #Your code here
                
    def getValue_by_Index(self,index):
        #Your code here
                
    def getValue_by_Key(self,key):
        #Your code here
        
    def delete_by_Value(self,val):
        #Your code here
        
    def delete_by_Index(self,val):
        #Your code here
        
    def delete_by_Key(self,val):
        #Your code here
    
    def print_all_keyValues(self):
        #Your code here

    def insert_at_First(self,key,val):
        #Your code here
            
    def insert_at_Last(self,key,val):
        #Your code here
    

    def length(self):
        if self.head != None and self.tail != None:
            return self.tail.index + 1
        else:
            return "Note: Table is Empty!"



# test cases               
d1 = HashTable()

d1.insert_at_First("csulb",1)
d1.insert_at_First("CECS",2)
d1.insert_at_First("CECS274",3)
d1.insert_at_Last("CS",4)
d1.insert_by_Index(1,"life",12)
d1.insert_by_Index(0,"time",44)
d1.insert_by_Index(3,"value",12)
d1.insert_by_Index(4,"good",26)
d1.insert_by_Index(4,"eng",27)
d1.delete_by_Value(8)
d1.delete_by_Index(1)
d1.delete_by_Key("time")
d1.insert_at_First("why",24)
d1.insert_at_Last("how",57)
d1.insert_by_Index(3,"know",145)
d1.insert_by_Index(4,"yes",243)



print("HashTable: ",end="")
d1.print_all_keyValues()
print("Length:",d1.length())
print("Value at Key 'eng':",d1.getValue_by_Key("eng"))
print("Value at Key 'csulb':",d1.getValue_by_Key("csulb"))
print("Value at index 3:",d1.getValue_by_Index(3))
print("Value at index 7:",d1.getValue_by_Index(7))





