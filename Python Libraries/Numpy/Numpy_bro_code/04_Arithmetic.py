import numpy as np 

array = np.array([1.1, 2.1, 3.9])


#Scalar and Vectorized Math fn's are both linear algebra terms, but Scalar(single value) and Vector(one dimension like a 1-D list)

##Scalar Arithmetic

print(array + 2)
print(array - 3)
print(array * 4)
print(array / 5)
print(array ** 2)
print(array // 2, end = "\n\n")

##Vectorized Math functions(Applying a fn on an array directly without running a loop)


###1-- ops on array
print(np.sqrt(array))
print(np.round(array))
print(np.ceil(array))
print(np.floor(array), end = "\n\n")

###2-- Printing constans
print(np.pi)
print(np.e, end = "\n\n")


##Practice q-- Given an array(radii of circle), form an array(area of circle)
##Solution--

radii = np.array([1, 2, 3])

###M1

PI = np.pi

radii_sq = np.pow(radii, 2)
area = radii_sq * PI

print(area)

###M2
radii_2 = np.array([1, 2, 3])
print(np.pi * radii_2 ** 2, end = "\n\n")


##Element-wise Arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)
print(array1 // array2, end = "\n\n")

##Comparison Operators(Using these we can create boolean arrays, filter data and do element-wise comparisons)

marks = np.array([10, 20, 30, 60, 70, 20, 100, 92])

print(marks > 60) # Returns a boolean array
print(marks == 10) # Returns a boolean array


##Assignment on basis of comparison

marks[marks >= 60] = 0
print(marks)







