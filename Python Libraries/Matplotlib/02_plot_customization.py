import matplotlib.pyplot as plt 
import numpy as np 


#plot customization

x = np.array([2023, 2024, 2025, 2026]) #years
y1 = np.array([10, 16, 12, 13]) #class-sizes

y2 = np.array([40, 16, 90, 3])
y3 = np.array([5, 15, 25, 35])

#Storing the attributes for plot customization in a dictionary and then unpacking the dictionary

#Attributes--

# a- marker
# b- markersize / ms
# c- markerfacecolor / mfc
# d- markeredgecolor / mec
# e- linestyle
# f- color
# g- linewidth

#for color-- color picker can be used

customize = dict(marker = "o",
                 ms = 10,
                 mfc = "red",
                 mec = "blue",
                 linestyle = "dashdot",
                 linewidth = 3)

plt.plot(x, y1, color = "cyan", **customize)
plt.plot(x, y2, color = "green", **customize)
plt.plot(x, y3, color = "black", **customize)

plt.show()



