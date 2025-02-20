def bubble_sort(array):
    for j in range(len(array)-1):
        for i in range( len(array)-1-j ):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array
l = [i for i in range(1000,1,-1)]

def bubble_sort_optimised(array):
    for j in range(len(array)-1):
        sorted = True
        for i in range( len(array)-1-j ):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
            if sorted :
                return
    return array
l = [i for i in range(1000,1,-1)]
#print(l)
print(bubble_sort(l))
