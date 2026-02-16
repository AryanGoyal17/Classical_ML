import numpy as np 

#Aggregate functions = Summarize data and typically return a single value...

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])


#1- Sum
print(np.sum(array))
#2- Mean
print(np.mean(array))
#3- Standard Deviation
print(np.std(array))
#4- Variance
print(np.var(array))
#5- Minimum Value
print(np.min(array))
#6- Maximum Value
print(np.max(array))
#7- Position of minimum value
print(np.argmin(array))
#8- Position of maximum value
print(np.argmax(array), end = "\n\n")

#9-- SELECTING AN AXIS(IMPORTANT!!)
print(np.sum(array, axis = 0))#Applied on columns
print(np.sum(array, axis = 1))#Applied on rows