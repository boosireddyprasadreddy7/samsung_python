'''
Boys and question is in sir's repo and folder is assingnments
'''
def can_arrange_students(num_cases, cases):
    results = []
    
    for case in cases:
        n = case[0] 
        boys = sorted(case[1]) 
        girls = sorted(case[2])  
        def is_valid(start_with_boy):
            arranged = []
            i, j = 0, 0
            is_boy_turn = start_with_boy
            
            while i < len(boys) or j < len(girls):
                if is_boy_turn:
                    if i < len(boys):
                        arranged.append(boys[i])
                        i += 1
                    else:
                        return False 
                else:
                    if j < len(girls):
                        arranged.append(girls[j])
                        j += 1
                    else:
                        return False 
                is_boy_turn = not is_boy_turn 
            return arranged == sorted(arranged) 
        if is_valid(True) or is_valid(False):
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Reading input
num_cases = int(input().strip())

cases = []
for _ in range(num_cases):
    n = int(input().strip())  # number of boys and girls
    boys = list(map(int, input().strip().split()))
    girls = list(map(int, input().strip().split()))
    cases.append((n, boys, girls))

# Calling the function to get results
results = can_arrange_students(num_cases, cases)

# Output results
for result in results:
    print(result)
