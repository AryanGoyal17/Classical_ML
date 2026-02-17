import numpy as np 

#Some Important numpy functions--

##1-- zeros(not zeroes), ones (to create a np array with 0 and 1, argument = shape of array)


# arr1 = np.zeros(2,2) #error
arr1 = np.zeros((2,2))
print(arr1, end = "\n\n")

arr2 = np.ones((2, 3, 10))
print(arr2, end = "\n\n")

##2-- full (For number > 1(function same as zeros and ones)) (arguments = (shape), value )

arr3 = np.full((2, 3, 10), 9)
print(arr3, end = "\n\n")

##3-- eye(create an identity matrix, argument = order of matrix)

arr4 = np.eye(4)
print(arr4, end = "\n\n")

arr5 = np.eye(2)
print(arr5, end = "\n\n")

##4-- empty(create an empty matrix with garbage values, argument = shape, faster than zeros, ones, full)

arr6 = np.empty((2,3))
print(arr6, end = "\n\n")

##5-- arange(NOT arrange)[arguments = start, stop, step(default = 1)]

arr7 = np.arange(1, 10)
print(arr7, end = "\n\n")

arr8 = np.arange(1, 10, 3)
print(arr8, end = "\n\n")

##6-- linspace(arguments = start, stop, no of points req(spacing calculated automatically by numpy))

arr9 = np.linspace(1, 10, 3)
print(arr9, end = "\n\n")

arr10 = np.linspace(1, 10, 7)
print(arr10, end = "\n\n")


##NOTE: In arange (stop is exclusive), In linspace (stop is NOT exclusive)
##