import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1, 4))
array3 = np.zeros((2, 5))

print(array1[4]) # IndexError
print(array1[0][0]) # SyntaxError array2 is not 2D
print(array2[2][0]) # IndexError
print(array3[3][3]) # IndexError