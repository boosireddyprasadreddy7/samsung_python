import random

user_name = int(input("ENter your Choice(1 to 10): "))
system_number = random.randint(0, 9)
if system_number != user_name :
    print("CrorePati")
else :
    print("RoadPati")