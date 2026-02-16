import numpy as np 

#Filtering-- Refers to the process of selecting elements from an array that match a given condition

array1 = np.array([[10,20,30,40,50],
                   [60,70,80,90,100]])

marks_pass = array1[array1 >= 40] #This is called boolean indexing(Original array(array-1) is preserved)
print(marks_pass)

marks_btw1 = array1[(array1 >= 40) & (array1 <= 60)] #As numpy uses C style arrays, use &(AND), |(OR) instead of and(AND), or(OR)
print(marks_btw1)

marks_error = array1[array1 > 100]
print(marks_error, end = "\n\n")#output array is empty


#Boolean indexing used above flattens out the given array, To preserve the original shape use the where fn
#Where fn is Slower than Boolean Indexing
#Syntax -- np.where(condition, array_name, fill_value) [fill value is the val to be placed in place of those who dont satisfy the condition]


#M1(To preserve the shape), (Also preserves the original array)
marks_fail = np.where(array1 < 40, array1, 0)
print(marks_fail)

#M2(To preserve the shape), (DOES NOT preserve the original array)
array1[array1 >= 40] = 0
print(array1)
