def merge_sort(array, low, high):
    if low < high :
        mid = low + (high + low) // 2
        merge_sort(array, low, mid-1)
        merge_sort(array, mid, high)
        merge(array, low, mid, high)
    return array
def merge(array, low, mid, high):
    array1 = array[1:mid+1]
    array2 = array[mid:]
    merged_array = []
    k = 0
    i = 0
    j = 0
    while i<j and j<high:
        if array1[i] < array2[j]:
            if array1[i] < array2[j]:
                merged_array[k] =  array1[i]
			    
                i += 1
		
            else:
			    
                merged_array[k] =  array1[j]
			    
                j += 1
		    
            k += 1
	
    merged_array += array1[i:]
	
    merged_array += array1[j:]
print(merge_sort([78,34,21], 0, 2))


'''
def merge_sort(numbers, low, high):
	if low < high:
		mid (low + (high - low) // 2)
		//mid = (low + high) // 2
		merge_sort(numbers, low, mid-1)
		merge_sort(numbers, mid, high)
		merge(numbers, low, mid, high)

# while i < len(array1) and j < len(array2):
	
def merge(numbers, low, mid, high):
	Copy 1st half of the array into array1
	Copy 2nd half of the array into array2
	
	merged_array = []
	k = 0
	i = low
	j = mid
	while array1 and array2 has numbers:
		if array1[i] < array2[j]:
			merged_array[k] =  array1[i]
			i += 1
		else:
			merged_array[k] =  array1[j]
			j += 1
		k += 1
	merged_array += array1[i:]
	merged_array += array1[j:]

'''