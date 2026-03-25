import pandas as pd 

df = pd.read_csv(r"D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv")

#Here, i have listed ways to rectify some errors faced while working with a dataset sometimes..

#1-- The Problem: You try to access df["Name"] but Python screams KeyError.
#     Why? Because the column is actually named " Name " or "Name ".

# print(df["Name"], end = "\n\n") #This results in KeyError...

#Solution--

# STRIP COLUMN NAMES
# This removes empty spaces from the start and end of every column name
df.columns = df.columns.str.strip()
print(df["Name"], end = '\n\n')
print(df["Height(m)"], end = "\n\n")

# 2-- How to display actual column names??

print(df.columns.tolist(), end = "\n\n") #Spaces before column name removed