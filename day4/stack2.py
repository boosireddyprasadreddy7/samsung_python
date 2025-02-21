import sys
#Inserting at end and deleting at end

class Stack:
    def __init__(self, size=5):
        self.stk = []
        self.size = size
        print("Empty Stack is created")
    def push(self):
        if len(self.stk) == self.size:
            print("Stack is full")
        else:
            element = input("Enter the element to be pushed")
            self.stk.append(element)
    def pop(self):
        if not self.stk:
            print("Stack is empty")
        else:
            print(f"Popped element is {self.stk.pop()}")
    def list_stack(self):
        if not self.stk:
            print("Stack is empty")
        else :
            print("The Stack elements: ", self.stk[::-1])


class Menu:
    def __init__(self): 
        pass
    def get_menu(self, stack):
        menu = {
            1 : stack.push,
            2 : stack.pop,
            3 : stack.list_stack,
            4 : self.end_of_program
        }
        return menu
    def end_of_program(self):
        sys.exit("Exit")
    def invalid_choice(self):
        print("Invalid choice")
    def run_menu(self):
        stack = Stack()
        while(True):
            choice = int(input("1.Push, 2.pop, 3.Display,-1.To Exit: "))
            if choice == -1 :
                break
            menu = self.get_menu(stack)
            menu.get(choice, self.invalid_choice)()
        print("End of Program")


menu = Menu()
menu.run_menu()