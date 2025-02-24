class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_position(self, data,position):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
        i = 0
        temp_node = self.head
        while temp_node.next is not None and i > position:
            temp_node = temp_node.next
            i += 1
        new_node.next = temp_node.next
        temp_node.next = new_node
         
    def insert(self, data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
        
        temp_node = self.head
        while temp_node.next is not None :
            temp_node = temp_node.next
            

        temp_node.next = new_node


    def delete_at_position(self, position):
        if not self.head: 
            print("List is empty!")
            return       
        temp = self.head
        if position == 0:
            self.head = temp.next  
            temp = None 
            return

        prev = None
        count = 0
        while temp and count < position:
            prev = temp
            temp = temp.next
            count += 1
        if temp is None:
            print("Position out of range!")
            return
        prev.next = temp.next  # Unlink the node
        temp = None  # Free memory
    def display(self):
        temp_node = self.head
        while temp_node != None :
            print(temp_node.data, " -> ", end='')
            temp_node = temp_node.next
        print()
    def display_reverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

llist = LinkedList()
llist.insert(10)
llist.insert(20)
llist.insert(30)
llist.delete_at_position(1)
#llist.insert_position(10,0)
llist.insert_position(40,2)
#llist.insert_position(30,2)
llist.display()
llist.display_reverse()
#llist.delete_position(2)