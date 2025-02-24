class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def merge_at_position(self, other_list, position):
        if not self.head:
            print("First list is empty, cannot merge.")
            return
        
        temp = self.head
        count = 0

        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range!")
            return

        rest = temp.next

        temp.next = other_list.head

        temp2 = other_list.head
        while temp2 and temp2.next:
            temp2 = temp2.next

        if temp2:
            temp2.next = rest


ll1 = LinkedList()
ll2 = LinkedList()

ll1.insert_at_end(1)
ll1.insert_at_end(2)
ll1.insert_at_end(3)
ll1.insert_at_end(4)

ll2.insert_at_end(100)
ll2.insert_at_end(200)
ll2.insert_at_end(300)

print("First Linked List:")
ll1.display() 

print("Second Linked List:")
ll2.display()

ll1.merge_at_position(ll2, 2)

print("Merged Linked List:")
ll1.display()  
