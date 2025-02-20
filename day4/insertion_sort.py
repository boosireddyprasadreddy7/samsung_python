import sys

def insertion_sort(strings):
    for i in range(1, len(input_list)):
        element = strings[i]
        j = i-1
        while j >= 0 and element.lower() < strings[j].lower():
            strings[j+1] = strings[j]
            j -= 1
        strings[j+1] = element
    return strings

input_list = sys.argv[1:]
print('User given strings are: \n', input_list)

sorted_list = insertion_sort(input_list)
print('Sorted strings are: \n', input_list)
def insert_sort_own(array):
    for i in range(1, len(array)):
        for j in range (i):
            if array[i-j] < array[i-j-1] :
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
            else :
                break
    return array

#print(insert_sort_own([4,7,1,34,6,90]))
print(insertion_sort([4,7,1,34,6,90]))
















