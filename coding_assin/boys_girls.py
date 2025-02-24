'''
Boys and question is in sir's repo and folder is assingnments
'''
def can_arrange(boys, girls):
    boys.sort()
    girls.sort()
    boys_first = True
    for i in range(len(boys)):
        if boys[i] > girls[i]:  
            boys_first = False
            break 
    girls_first = True
    for i in range(len(girls)):
        if girls[i] > boys[i]:  
            girls_first = False
            break 
    if boys_first or girls_first:
        return "YES"
    else:
        return "NO"

b = [5, 3, 8]
g = [2, 4, 6]
print(can_arrange(b, g))