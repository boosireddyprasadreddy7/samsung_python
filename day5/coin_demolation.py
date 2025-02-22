amount = int(input("Enter the amount you want: "))
def return_coins(amount):
    coins = {"coin10" : 0,
             "coin5" : 0,
             "coin2" : 0,
             "coin1" : 0
             }
    
    while amount > 0:
        if amount % 10 == 0 :
            coins["coin10"] += 1
            amount = amount - 10
        elif amount % 5 == 0 :
            coins["coin5"] += 1
            amount = amount - 5
        elif amount % 2 == 0 :
            coins["coin2"] += 1
            amount = amount - 2
        else :
            coins["coin1"] += 1
            amount = amount - 1
    return coins
print(return_coins(amount=97))