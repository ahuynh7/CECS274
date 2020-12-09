class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.next = None;    
     
class CreateList:    
 
    def __init__(self):    
        # Youe code here 
        
   
    def add(self,data):    
        # Youe code here
    


    #This function will print the nodes of circular linked list from the head
    def print(self):
        # Youe code here



    #This function will count the nodes of circular linked list    
    def countNodes(self):    
        # Youe code here
        
     
class CircularLinkedList:    
    cl = CreateList();    
    #Adds data to the list    
    cl.add(4);    
    cl.add(5);    
    cl.add(7);    
    cl.add(8);    
    cl.add(12);    
    cl.add(56);   
    cl.add(85);
    cl.add(41); 
    #Displays all the nodes present in the list   
    cl.print();
    cl.countNodes();
