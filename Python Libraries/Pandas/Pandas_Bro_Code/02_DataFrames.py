import pandas as pd 

#DataFrame -- A tabular data structure with rows and columns (2-D), like excel spreadsheet


#1-- Creating a dataframe
data1 = {"Name" : ["Aryan", "Arnav", "Amit"],
          "Age" : [20,30,40]}

df1 = pd.DataFrame(data1)
print(df1, end = "\n\n")

df2 = pd.DataFrame(data1, index = ["Employee1", "Employee2", "Employee3"])
print(df2, end = "\n\n")

#2-- Using loc and iloc..

#loc
print(df2.loc["Employee3"], end = "\n\n")

#iloc

print(df2.iloc[0], end = "\n\n")

#3-- Creating new rows and columns..

#A-- creating a new column

df2["Job"] = ["Cashier", "Engineer", "N/A"]
print(df2, end = "\n\n")

#B-- Creating a new row

new_row1 = pd.DataFrame([{"Name": "Shekhar", "Age" : 40, "Job" : "N/A"}])
df2 = pd.concat([df2, new_row1])
print(df2, end = "\n\n")

#To give a pre-defined index to the new row

new_row2 = pd.DataFrame([{"Name" : "Akhil", "Age" : 1, "Job" : "Crying"}], index = ["Employee4"])
df2 = pd.concat([df2, new_row2])
print(df2, end = "\n\n")

#C-- Creating multiple rows

new_row3 = pd.DataFrame([{"Name" : "Manpreet", "Age" : 67, "Job" : "Doctor"},
                         {"Name" : "Jagdeep", "Age" : 76, "Job" : "Teacher"}], index = ["Employee5", "Employee6"])

df2 = pd.concat([df2, new_row3])

print(df2, end = "\n\n")

##