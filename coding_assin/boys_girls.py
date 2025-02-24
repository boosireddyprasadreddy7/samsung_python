'''
Boys and question is in sir's repo and folder is assingnments
'''
def can_arrange(boys, girls):
    boys.sort()
    girls.sort()

    def valid_arrangement(first, second):
        for i in range(len(first)):
            if first[i] > second[i]: 
                return False
        return True
    if valid_arrangement(boys, girls) or valid_arrangement(girls, boys):
        return "YES"
    else:
        return "NO"

b = [5, 3, 8]
g = [2, 4, 6]
print(can_arrange(b, g))
