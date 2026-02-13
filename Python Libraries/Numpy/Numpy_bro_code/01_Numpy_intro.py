import numpy as np 

#Trying to multiply a list by 2

list1 = [1,2,3,4]
print(list1 * 2) #Doesnt multiply the elements
print(type(list1))
print('\n')

#Now using numpy arrays(faster than python lists)

array1 = np.array(list1)
print(array1)
print(array1 * 2)
print(type(array1)) #numpy = np, nd = n-dimensional
