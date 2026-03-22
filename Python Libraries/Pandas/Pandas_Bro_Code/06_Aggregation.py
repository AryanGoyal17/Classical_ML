import pandas as pd 

# aggregate functions = reduce a set of values into a single summary value.
#                       Used to summarize and analyze data
#                       Often used with the groupby() function

df = pd.read_csv(r"D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv")

df.columns = df.columns.str.strip()

#On whole dataframe

print(df.mean(numeric_only=True), end = "\n\n")
print(df.sum(numeric_only=True), end = "\n\n")
print(df.min(numeric_only=True), end = "\n\n")
print(df.max(numeric_only=True), end = "\n\n")
print(df.count(), end = "\n\n")

#On a single column

print(df["Weight(kg)"].mean())
print(df["Weight(kg)"].sum())
print(df["Weight(kg)"].min())
print(df["Weight(kg)"].max())
print(df["Type2"].count(), end = "\n\n")

#group-by

group = df.groupby("Type1") #Pokemons are grouped on the basis of their 1st type
print(group, end = "\n\n")#an object..

print(group["Height(m)"].mean())
print(group["Height(m)"].sum())
print(group["Height(m)"].min())
print(group["Height(m)"].max())
print(group["Height(m)"].count())

