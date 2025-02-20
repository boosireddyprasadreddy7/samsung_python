import sys
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
            self.stk.insert(0, element)
    def pop(self):
        if not self.stk:
            print("Stack is empty")
        else:
            print(f"Popped element is {self.stk[0]}")
            del self.stk[0]
    def list_stack(self):
        if len(self.stk) == self.size:
            print("Stack is full")
        else :
            print("The Stack elements: ", self.stk)

#class Event:
#    def monday(self):
#        print("Today is Technical fest")
#    def tuesday(self):
#        print("Today is dept fest")
#    def wednesday(self):
#        print("Today is Cultural fest")
#    def friday(self):
#        print("Today is Ethnic fest")
#    def other_day(self):
#        print("Invalid Choice")

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
        print("INvalid choice")
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