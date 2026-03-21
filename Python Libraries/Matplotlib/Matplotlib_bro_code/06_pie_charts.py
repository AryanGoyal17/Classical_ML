import matplotlib.pyplot as plt 
import numpy as np 

#Pie chart -- Circular chart divided into slices to show percentages of total
#             Good for visualizing distribution among categories

categories = ["Freshman", "Sophomore", "Juniors", "Seniors"]
num_students = np.array([500, 400, 371, 200])

colors = ["Green", "Orange", "Purple", "Red"] #if we want to give colors by ourselves

pie_customize = dict(autopct = "%1.1f%%", colors = colors, explode = [0,0,0,0.2], shadow = True, startangle = 90) #%1f is a formatting instruction
plt.pie(num_students, labels = categories, **pie_customize)

plt.title("Student distribution in a College", fontweight = "bold", family = "Arial")
plt.show()