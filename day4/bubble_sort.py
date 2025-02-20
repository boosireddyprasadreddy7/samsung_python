def bubble_sort(array_list):
    for j in range(len(array_list)-1):
        for i in range( len(array_list)-1-j ):
            if array_list[i] > array_list[i+1]:
                array_list[i], array_list[i+1] = array_list[i+1], array_list[i]
    return array_list
l = [i for i in range(1000,1,-1)]

def bubble_sort_optimised(array_list):
    for j in range(len(array_list)-1):
        sorted = True
        for i in range( len(array_list)-1-j ):
            if array_list[i] > array_list[i+1]:
                array_list[i], array_list[i+1] = array_list[i+1], array_list[i]
                sorted = False
        if sorted :
            return array_list
    return array_list
l = [i for i in range(1000,1,-1)]
#print(l)
print(bubble_sort(l))
print(bubble_sort_optimised(l))
