import matplotlib.pyplot as plt 
import numpy as np

#Scatter graphs -- Shows the relationship between 2 variables
#                  NOTE: Helps to identify a correlation (+, -, None)


#Example-- Hours Studied vs Marks obtained

#Class1

x1 = np.array([0, 1, 2, 3, 3, 4, 5, 8, 9, 10, 15])
y1 = np.array([10, 20, 25, 30, 50, 60, 80, 87, 93, 96, 99])

#Class2

x2 = np.array([0, 1, 2, 3, 4, 5, 5, 9, 9, 12])
y2 = np.array([10, 25, 26, 40, 42, 38, 52, 82, 87, 85])

plt.scatter(x1, y1, color = "red", alpha = 0.2, s = 140, label = "Class1")
plt.scatter(x2, y2, color = "darkgreen", alpha = 0.6, s = 140, label = "Class2")

plt.title("Study hours vs Marks obtained")
plt.xlabel("Study hours")
plt.ylabel("Marks obtained")

plt.legend()
plt.show()