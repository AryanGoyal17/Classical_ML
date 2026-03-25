import matplotlib.pyplot as plt 
import numpy as np 

#grid() helps make plots easier to read by adding reference lines.

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 60]

grid_attributes = dict(axis = "y", 
                       linestyle = "dashdot",
                       linewidth = 2,
                       color = "black")

plt.grid(**grid_attributes)

plt.plot(x, y)
plt.show()