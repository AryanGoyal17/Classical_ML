import numpy as np 

array = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]])

#Slicing rows(examples)

print(array[0:2], end = "\n\n")
print(array[1:4], end = "\n\n")
print(array[::2], end = "\n\n")
print(array[::-1], end = "\n\n") #Reversing rows

#Slicing columns(examples)

print(array[:, 0], end = "\n\n")
print(array[:, 1:3], end = "\n\n")
print(array[:, ::-1], end = "\n\n") #Reversing columns

#Slicing rows and columns together(examples)

print(array[0:2, 0:2], end = "\n\n")
print(array[1:3, 1:], end = "\n\n")
print(array[::-1, ::-1], end = "\n\n") #Both rows and columns reversed
print(array[1::2, 1::3], end = "\n\n") #IMPORTANT!!
