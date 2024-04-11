class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            new_node.prev=self.tail
            self.tail=new_node
            self.head.prev=self.tail
        self.length+=1
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            self.head.prev=self.tail
            self.tail.next=self.head
        self.length+=1
    
    def __str__(self):
        temp=self.head
        result=' '
        while temp:
            result+= str(temp.value)
            temp=temp.next
            if temp==self.head:
                break
            result+='<->'
        return result
    
    def travseral(self):
        temp=self.head
        while True:
            print(temp.value)
            temp= temp.next
            if temp==self.head:
                break
    
    def reverse_travseral(self):
        temp=self.tail
        while True:
            print(temp.value)
            temp= temp.prev
            if temp==self.tail:
                break
    
    def search(self,value):
        temp=self.head
        count=0
        while True:
            if temp.value==value:
                return True,count
            temp=temp.next
            if temp==self.head:
                break
            count+=1
        return False
        
    
    def get(self,index):
        temp=self.head
        if index<self.length//2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(index,self.length-1):
                temp=temp.prev
        return temp
    
    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def insert(self,index,value):
        temp=self.get(index-1)
        new_node=Node(value)
        new_node.next=temp.next
        new_node.prev=temp
        new_node.next.prev=new_node
        temp.next=new_node
        self.length+=1
    
    def pop_first(self):
        pop=self.head
        self.head=self.head.next
        pop.next=None
        pop.prev=None
        self.head.prev=self.tail
        self.tail.next=self.head
        self.length-=1
    
    def pop_method(self):
        pop=self.tail
        self.tail=self.tail.prev
        pop.next=None
        pop.prev=None
        self.tail.next=self.head
        self.length-=1
    
    def remove(self,index):
        poped=self.get(index)
        poped.prev.next=poped.next
        poped.next.prev=poped.prev
        poped.next=None
        poped.prev=None
        self.length-=1

    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0
        
new_linked_list=LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)
new_linked_list.prepend(60)
new_linked_list.reverse_travseral()
print(new_linked_list.search(10))
print(new_linked_list.get(5))
new_linked_list.set(3,69)
new_linked_list.insert(3,70)
new_linked_list.set(3,43)
new_linked_list.pop_first()
new_linked_list.pop_method()
new_linked_list.remove(3)
print(new_linked_list)
new_linked_list.travseral()