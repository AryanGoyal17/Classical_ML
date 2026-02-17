#dtype = Keyword argument that tells Numpy what kind of values are stored in an array.
#        Otherwise Numpy guesses the best data type based on your data
#        Manually setting dtype improves performance and is more memory efficient(especially when working with larger data sets)

import numpy as np 

#Data-types

#1-- Integer (int8, int16, int32, int64) #No after int denotes the no of bits taken by each element, 8bits = 1byte
#2-- Float (float16, float32, float64) #No after float denotes the no of bits taken by each element
#3-- Boolean (bool_)
#4-- String (str_, <U#)
#5-- Object (object_)



#1-- Integer

arr1 = np.array([1, 2, 3, 4, 5])

print(arr1)
print(arr1.dtype)
print(f"{arr1.nbytes} bytes", end = "\n\n")


#Manually assigning a data-type(by keyword argument of dtype)

arr2 = np.array([1,2,3,4,5], dtype = np.int32)

print(arr2)
print(arr2.dtype)
print(f"{arr2.nbytes} bytes", end = "\n\n")


#NOTE: Maximum value which a element of array can have decreases with the no of bits/element

# arr3 = np.array([126, 127, 128], dtype = np.int8) -- OverflowError: Python integer 128 out of bounds for int8
# print(arr3)


#NOTE:

# -------------------------------------------------------------------------
# INTEGER DATA TYPES & RANGES
# -------------------------------------------------------------------------
# The number of bits determines the range of values an array can hold.
# If you try to store a number larger than the Max, it will "overflow" (wrap around).

# int8  (8 bits)  : -128 to 127
# int16 (16 bits) : -32,768 to 32,767
# int32 (32 bits) : -2,147,483,648 to 2,147,483,647  (~ ±2 Billion)
# int64 (64 bits) : -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (~ ±9 x 10^18)


# 2-- Float(NOTE: float8 doesnt exist!!)

arr4 = np.array([1, 2, 3, 4, 5], dtype = np.float32)

print(arr4)
print(arr4.dtype)
print(f"{arr4.nbytes} bytes", end = "\n\n")

# 3-- Boolean(Anything which is non-zero returns True, 1 bool = 1byte)

arr5 = np.array([1, 2, 3, 4, 5, 0], dtype = np.bool_) #np.bool is also correct(synonym for np.bool_) but it might crash in older versions so prefer np.bool_
                                                      #np.bool referred to python boolean in older versions of numpy and took more memory but now its equal to np.bool_
print(arr5)
print(arr5.dtype)
print(f"{arr5.nbytes} bytes", end = "\n\n")

# 4-- String

arr6 = np.array([1, 2, 3, 4, 5, 0], dtype = np.str_)
print(arr6)
print(arr6.dtype)
print(f"{arr6.nbytes} bytes", end = "\n\n")
#<U1 = fixed size unicode string (here size = 1, 1 character = 4bytes)

arr7 = np.array(["Apple", "Banana", "Orange"], dtype = "<U4") #converts to unicode string of size = 4
print(arr7)
print(arr7.dtype)
print(f"{arr7.nbytes} bytes", end = "\n\n") #NOTE: numpy arrays (dtype = np.str_) , each character takes 4bytes

# 5-- Objects

## np.object_ is NumPy's "Catch-All" data type.
## When you try to put something into an array that isn't a simple fixed-size number (like a mix of strings, integers, and lists),
## NumPy gives up on trying to be efficient and falls back to np.object_.

## When we use np.object_ , we lose the numpy's improved performance and efficiency

arr8 = np.array([1, 67.67, "Hi", 67, True], dtype = np.object_)
print(arr8)
print(arr8.dtype)
print(f"{arr8.nbytes} bytes", end = "\n\n") 

#Why is the size 40bytes?

#Ans--
# This is a classic "pointer" calculation. The size is 40 bytes because of your computer's architecture, not the data itself.
# Here is the exact math behind it:

# 1. The Math
# Your System: You are on a 64-bit computer (which is standard today).

# Pointer Size: On a 64-bit system, a memory address (pointer) takes exactly 8 bytes.
# Array Length: Your array has 5 elements ([1, 67.67, "Hi", 67, True]).
# 5 elements * 8bytes(per pointer) = 40bytes


##### Type-Casting in Numpy


## Example-1
arr9 = np.array([1.1, 2.3, 4.5])

print(arr9)
print(arr9.dtype)
print(f"{arr9.nbytes} bytes")

arr9 = arr9.astype(np.int8) #Type-casted float to int
print(arr9)
print(arr9.dtype)
print(f"{arr9.nbytes} bytes", end = "\n\n")

## Example-2

arr10 = np.array([1,2,3])

print(arr10)
print(arr10.dtype)
print(f"{arr10.nbytes} bytes")

arr11 = arr10.astype(np.bool_) #Type-casted int to bool (in a new array)
print(arr11)
print(arr11.dtype)
print(f"{arr11.nbytes} bytes")

#Original array preserved

print(arr10)
print(arr10.dtype)
print(f"{arr10.nbytes} bytes")

##

