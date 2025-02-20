def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        
        while j >= 0 and array[len(array)-i] < array[j] :
            array[j], array[len(array)-i] = array[len(array)-i], array[j]
            j -= 1
 

    return array
def insert_sort_own(array):
    for i in range(1, len(array)):
        for j in range (i):
            if array[i-j] < array[i-j-1] :
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
            else :
                break
    return array

print(insert_sort_own([4,7,1,34,6,90]))

















