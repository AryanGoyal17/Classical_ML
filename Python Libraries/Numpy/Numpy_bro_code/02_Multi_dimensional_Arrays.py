import numpy as np 

#Numpy arrays can have various dimensions(0,1,2,3 etc..)

array0 = np.array('A')
print(array0.ndim) #to check dimension

array1 = np.array([1,2,3])
print(array1.ndim) #to check dimension


#2-d Arrays are like a matrix..(rows and columns)
array2 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(array2.ndim) #to check dimension

#3-d Arrays have rows, columns, depth(no of layers)

# array3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
#                   [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q']]])

#The above array gives an error as it becomes inhomogeneous after 2nd dimension....

array3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', '_']]]) #Type a placeholder like _ to avoid error

print(array3.ndim, end = "\n\n")

#.shape attribute

print(array0.shape)
print(array1.shape)
print(array2.shape)
print(array3.shape, end = "\n\n") # 2-layers, Each layer has 3 rows(each list is a row), and 3 columns


#Indexing(Chain indexing vs Multi-dimensional indexing)

## Multi-dimensional indexing is faster than chain indexing

print(array3[0][2][1]) #chain indexing
print(array3[0, 2, 1], end = "\n\n") #Multi-dimensional indexing


#Extra--

word = array3[0, 2, 1] + array3[0, 1, 1] + array3[1, 1, 1]
print(word)

