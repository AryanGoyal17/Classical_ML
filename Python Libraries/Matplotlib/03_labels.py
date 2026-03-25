import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([2023, 2024, 2025, 2026]) #years
y1 = np.array([10, 16, 12, 13]) #class-sizes

y2 = np.array([40, 16, 90, 3])
y3 = np.array([5, 15, 25, 35])

yticks = [10,20,30,40,50,60,70,80,90] #Not a np array but still works!

customize = dict(marker = ".",
                 ms = 10,
                 mfc = "red",
                 mec = "blue",
                 linestyle = "solid",
                 linewidth = 2)


title_customize = dict(fontsize = 20,
                       family = "Arial",
                       fontweight = "bold",
                       color = "Black")

label_customize = dict(fontsize = 10,
                       family = "Arial",
                       fontweight = "bold",
                       color = "Blue")

plt.title("Class Sizes across 2023-2026", **title_customize)

plt.xlabel("Year", **label_customize)
plt.ylabel("Class Size", **label_customize)

plt.tick_params(axis = "both", colors = "red") #axis = "x"/"y"/"both", #if color instead of colors , then only the markers of ticks red, not the numbers..

plt.xticks(x)
plt.yticks(yticks)

plt.plot(x, y1, color = "cyan", **customize)
plt.plot(x, y2, color = "green", **customize)
plt.plot(x, y3, color = "black", **customize)

plt.show()