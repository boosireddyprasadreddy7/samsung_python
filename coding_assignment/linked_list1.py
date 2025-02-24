class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        """Insert a node at the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, position):
        """Insert a node at a specific position in the linked list."""
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of range!")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    
    def delete_at_position(self, position):
        """Delete a node at a specific position."""
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        prev = None
        for _ in range(position):
            if temp is None:
                print("Position out of range!")
                return
            prev = temp
            temp = temp.next
        if temp is None:
            print("Position out of range!")
            return
        prev.next = temp.next
        temp = None
    
    def display(self):
        """Display the linked list in order."""
        temp = self.head
        while temp:
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")
    
    def display_reverse(self, node=None):
        """Display the linked list in reverse order using recursion."""
        if node is None:
            node = self.head
            if node is None:
                print("None")
                return
        if node.next:
            self.display_reverse(node.next)
        print(node.data, "->", end=" ")
        if node == self.head:
            print("None")

def menu():
    llist = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Insert at end")
        print("2. Insert at position")
        print("3. Delete at position")
        print("4. Display list")
        print("5. Display reverse")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data: "))
            llist.insert(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            position = int(input("Enter position: "))
            llist.insert_at_position(data, position)
        elif choice == 3:
            position = int(input("Enter position: "))
            llist.delete_at_position(position)
        elif choice == 4:
            llist.display()
        elif choice == 5:
            llist.display_reverse()
        elif choice == 6:
            break
        else:
            print("Invalid choice, please try again.")

menu()
