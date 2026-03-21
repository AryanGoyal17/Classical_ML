import matplotlib.pyplot as plt 
import numpy as np 

#Bar chart = compare categories of data by representing each category with a bar

#NOTE: Numpy doesnt make list of strings more efficient

categories = ["OpenAI", "Anthropic-AI", "xAI", "Google Deepmind"]
revenue = np.array([10, 900, 15, 100])

plt.bar(categories, revenue)

plt.title("Sales of AI companies")
plt.xlabel("Company")
plt.ylabel("Revenue")
plt.show()

plt.barh(categories, revenue, color = "red") #Horizontal bar chart

plt.title("Sales of AI companies")
plt.xlabel("Revenue")
plt.ylabel("Company")
plt.show()