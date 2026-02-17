#Reshape -- Changes the shape of an array without changing its underlying data.
#           .reshape(rows, columns) (to reshape to 2D array)
#           .reshape(layers, rows, columns) (to reshape to 3D array)

import numpy as np 

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr1.shape)

# arr1 = arr1.reshape(3,5)
# print(arr1.shape)
# print(arr1, end = "\n\n") #Original array changed

arr2 = arr1.reshape(3, 4)
print(arr2.shape)
print(arr2, end = "\n\n") #Original array preserved(reshaped to 2-D)

arr3 = arr1.reshape(3, 2, 2)
print(arr3.shape)
print(arr3, end = "\n\n") #Original array preserved(reshaped to 3-D)

#Important(Errors)

#1-- arr1.reshape(3,3,4)
#3-- arr1.reshape(2, 4) ValueError: cannot reshape array of size 12 into shape (2,4)
#3-- arr1.reshape(3, 5) etc...


#If a row/column/layer is assigned a value of -1 Numpy calculates the appropriate value

arr4 = arr1.reshape(-1, 2, 3)
print(arr4.shape)
print(arr4, end = "\n\n")

arr5 = arr1.reshape(-1, 6)
print(arr5.shape)
print(arr5, end = "\n\n")

##

