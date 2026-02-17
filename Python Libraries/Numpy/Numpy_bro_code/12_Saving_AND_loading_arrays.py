import numpy as np 

##1--
#Saving a numpy array(can use a absolute/relative file path(use double backlashes with the file path))
#Will file path not specified, by default array is stored in same parent folder as the code

array1 = np.array([[1,2,3], [4,5,6]])
np.save("Data1", array1) #arguments = filename, arrayname
np.save("C:\\Users\\aryan\\OneDrive\\Pictures\\Camera Roll\\Data1", array1)

print("Numpy array saved successfully", end = "\n\n") #Confirmation Message

##2--
#Loading a numpy array

array2 = np.load("C:\\Users\\aryan\\OneDrive\\Pictures\\Camera Roll\\Data1.npy")
print(array2)
print("Array was loaded successfully", end = "\n\n")


##3--
#Saving Multiple arrays(use np.savez("File name", name of arrays))

array3 = np.array([[1,2,3], [4,5,6]])
array4 = np.array([1,2,3])

np.savez("Data_multiple", array3, array4) #z = zipped

np.savez_compressed("Data_Multiple_compressed", array3, array4) #This is saved as a compressed zip folder(uses less memory)
                                                                #But compressed data loads slowly compared to non-compressed one
                                                                #Use it when data is large

print("Arrays were saved successfully", end = "\n\n") #Confirmation message

#Loading multiple arrays

arrays1 = np.load("Data_multiple.npz") #Relative file path works. Why?(look at the current working directory in terminal)
arrays2 = np.load("Data_Multiple_compressed.npz")
print(arrays1)
print(arrays2)


print(arrays1["arr_0"], end = "\n\n")
print(arrays2["arr_1"], end = "\n\n")

print("Arrays were loaded succesfully!!!!")
##

