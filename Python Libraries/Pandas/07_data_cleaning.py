#Data-Cleaning..

import pandas as pd 

df = pd.read_csv(r"D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv")

df.columns = df.columns.str.strip()

print(df, end = "\n\n")

#Data-cleaning-- the process of fixing/removing:
#                incomplete, incorrect or irrelevant data.
#                75% of work done with pandas is data cleaning..


#1-- Drop irrelvant columns

# df1 = df.drop(columns = ["Legendary"])
df1 = df.drop(columns = ["Legendary", "Number"])
print(df1, end = "\n\n")

#2-- Handle missing data

df2 = df.dropna(subset = ["Type2"]) #dropping those rows which dont have a type2
print(df2, end = "\n\n")

df3 = df.fillna({"Type2" : "None"}) #Assigning type2 as none for those pokemons which dont have a type2
print(df3, end = "\n\n")

#3-- Fix inconsistent values

df3["Type1"] = df3["Type1"].replace({"grass" : "GRASS", "rock" : "ROCK"})
print(df3, end = "\n\n")

#4-- Standardize data

df3["Name"] = df3["Name"].str.lower()
print(df3, end = "\n\n")

#5-- Fix data types

df3["Legendary"] = df3["Legendary"].astype(bool)
print(df3, end = "\n\n")

#6-- Remove duplicates--

df3 = df3.drop_duplicates()
print(df3, end = "\n\n")