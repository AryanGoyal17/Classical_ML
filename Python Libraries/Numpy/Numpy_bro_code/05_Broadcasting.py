##IMPORTANT!!!

import numpy as np 

#Broadcasting(NOTE:)

## Broadcasting allows Numpy to perform operations on arrays with different shapes by virtually expanding dimensions so they match
## the larger array's shape.


##RULES FOR BROAD-CASTING:
## The dimensions have the same size
## OR
## One of the dimensions has a size of 1. 

##Important Examples--
#1-- (1,4) and (4,1) can be broadcasted
#2-- (3,2) and (3,1) can be broadcasted
#3-- (1,4) and (3,4) can be broadcasted

#4-- (1,2) and (1,3) can NOT be broadcasted(program crashes, error shown (operands cant be broadcasted))

arr1 = np.array([[1,2,3,4]])
arr2 = np.array([[1], [2], [3], [4]])

print(arr1.shape)
print(arr2.shape, end = "\n\n")
#Can be broadcasted!!

print(arr1 + arr2, end = "\n\n") #Broadcasting occurs , arrays stretched(4x4 matrix formed)

arr3 = np.array([[1,2,3]])
print(arr1.shape)
print(arr3.shape, end = "\n\n")#Cant be broadcasted

# print(arr1 + arr3) #ValueError: operands could not be broadcast together with shapes (1,4) (1,3)


##EXAMPLE----- Create a multiplication table using numpy arrays and broadcasting

#M1
num = int(input("Enter the number whose multiplication table you want: "))

arr_ex1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arr_ex2 = np.array([[num]])

print(arr_ex1 * arr_ex2, end = "\n\n")

#M2

arr1_M2 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2_M2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(arr1_M2 * arr2_M2)



