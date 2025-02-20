number_of_oranges = int(input("Enter the number of oranges: "))
list_of_oranges = list( map(int,input("Enter the list oranges size: ").split()))
def quick_sort(list_of_oranges):
    k = 0
    for i in range(0, len(list_of_oranges)-1):
        if list_of_oranges[i] <= list_of_oranges[-1] :
            list_of_oranges[i], list_of_oranges[k] = list_of_oranges[k], list_of_oranges[i]
            k += 1

    list_of_oranges[-1], list_of_oranges[k] = list_of_oranges[k], list_of_oranges[-1]
    return list_of_oranges
print(list_of_oranges)