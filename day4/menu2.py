class Event:
    def monday(self):
        print("Today is Technical fest")
    def tuesday(self):
        print("Today is dept fest")
    def wednesday(self):
        print("Today is Cultural fest")
    def friday(self):
        print("Today is Ethnic fest")
    def other_day(self):
        print("Invalid Choice")

class Menu:
    def __init__(self): 
        pass
    def get_menu(self, events):
        menu = {
            1 : events.monday,
            2 : events.tuesday,
            3 : events.wednesday,
            4 : events.friday
        }
        return menu
    def run_menu(self, events):
        while(True):
            choice = int(input("1.Monday, 2.Tuesday, 3.wednesday, 4.Friday, -1.To Exit: "))
            if choice == -1 :
                break
            menu = self.get_menu(events)
            menu.get(choice, events.other_day)()
        print("End of Program")

event = Event()
menu = Menu()
menu.run_menu(event)