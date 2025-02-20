def monday():
    print("Today is Technical fest")
def tuesday():
    print("Today is dept fest")

def wednesday():
    print("Today is Cultural fest")
def friday():
    print("Today is Ethnic fest")
def other_day():
    print("Invalid Choice")
menu = {
    1 : monday,
    2 : tuesday,
    3 : wednesday,
    4 : friday
}
while(True):
    choice = int(input("1.Monday, 2.Tuesday, 3.wednesday, 4.Friday, -1.To Exit: "))
    
    if choice == -1 :
        break
    menu.get(choice, other_day)()