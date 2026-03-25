import matplotlib.pyplot as plt 
import numpy as np 

#Figure -- refers to the entire canvas
#Ax -- A single plot(subplot)

x = np.array([1,2,3,4,5])

y = ["ChatGPT", "Gemini", "Claude"]
z = np.array([400, 300, 1000])

subjects = ["Manpro", "ED", "Profcom", "Maths"]
scores = np.array([10, 20, 30, 90])
#To see what is stored in plt.subplots and gets unpacked afterwards....
# print(plt.subplots(2,2))

figure, axes = plt.subplots(2,2)

axes[0,0].plot(x, x**2, color = "red") # y = x^2
axes[0,0].set_title("y = x^2")

axes[1,0].bar(y, z, color = "blue")
axes[1,0].set_title("Company sales")

axes[0,1].plot(x, x*3, color = "green") #y = 3x
axes[0,1].set_title("y = 3x")

axes[1,1].pie(scores, autopct = "%1.1f%%", shadow = True, labels = subjects, explode = [0.1, 0.1, 0.1, 0.1])
axes[1,1].set_title("Marks percentages in different subjects")

plt.tight_layout()
plt.show()