class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, list_number):
        self.head = None
        print(f'LinkedList-{list_number} has been created')
    
    def addNodeAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

def createLinkedList(list_number):
    linked_list = LinkedList(list_number)
    print(f'Creating LinkedList-{list_number}')
    while True:
        data = input('Enter data for the new node: ')
        linked_list.addNodeAtFront(data)
        choice = input('Enter 1 to add another node, any other number to stop: ')
        if choice != '1':
            break
    return linked_list

def checkListsIntersect(list1, list2):
    if not list1.head or not list2.head:
        print('The linked lists do not intersect')
        return -1
    
    temp1, temp2 = list1.head, list2.head
    position = 0
    while temp1 and temp2:
        if temp1 == temp2:
            return position
        temp1 = temp1.next
        temp2 = temp2.next
        position += 1
    return -1

list1 = createLinkedList(1)
list2 = createLinkedList(2)
intersection_position = checkListsIntersect(list1, list2)
if intersection_position == -1:
    print('The linked lists do not intersect')
else:
    print(f'The linked lists intersect at position {intersection_position}')