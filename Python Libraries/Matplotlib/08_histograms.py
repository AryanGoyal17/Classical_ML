import matplotlib.pyplot as plt 
import numpy as np 

#Histograms -- A visual representation of distribution of quantitative data.
#              They group values into bins(intervals)
#              and counts how many values fall in each range.abs

scores = np.random.normal(loc = 80, scale = 10, size = 100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, color = "cyan", bins = 10, edgecolor = "black")

plt.title("Marks distribution of students of a class")
plt.xlabel("Marks")
plt.ylabel("No of students")

plt.show()