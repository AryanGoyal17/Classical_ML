##Checking the version

#import matplotlib
# print(matplotlib.__version__) To check version


import matplotlib.pyplot as plt 
import numpy as np

#pyplot -- module inside matplotlib which provides user friendly interface for plotting

##
# x = [2023, 2024, 2025, 2026] #years
# y = [10, 16, 50, 13] #class-sizes

##1--Use numpy arrays as they are faster

x = np.array([2023, 2024, 2025, 2026]) #years
y = np.array([10, 16, 12, 13]) #class-sizes

#2--DONT put 2 plt.plots in same line.. as they dont give intended results

##plt.plot(x, y) #first argument -- points in x axis, second argument -- points in y axis. 
##plt.plot(y)

#3--
plt.plot(x, y) #first argument -- points in x axis, second argument -- points in y axis.
plt.show() # to show the plot

#4--
##If only 1 argument is given, it is taken as values of y axis, and x axis -- takes as 0,1,2,3...
plt.plot(x)
plt.show()

plt.plot(y)
plt.show()

