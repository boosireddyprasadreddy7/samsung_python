import binary_search
import sys

print(f"The Input Number are are \n {sys.argv[1:-1]}")
print(f"The Search element is {sys.argv[-1]}")
search_element_index = binary_search.binarySearch(sys.argv[1:-1], sys.argv[-1])

if search_element_index == -1 :
    print(f"The search element {sys.argv[-1]} is not found")
else:
    print(f"The search element {sys.argv[-1]} was found at index {search_element_index}")