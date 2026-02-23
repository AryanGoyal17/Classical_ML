import pandas as pd 

#1-- Selection of Column

df = pd.read_csv(r"D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv")

print(df[" Height(m)"], end = "\n\n") #Use .to_string() to see all

#2-- Selection of multiple columns

print(df[[" Name", " Height(m)"]], end = "\n\n")

#3-- Selection of row

#A
print(df.loc[0], end = "\n\n")

#B
#In large datasets like this, we can use names (here pokemon names) as index!!

df2 = pd.read_csv(r"D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv", index_col = " Name")
print(df2.loc["Pikachu"], end = "\n\n") #Here the name column becomes the index column

#C
#If we want only some info of a pokemon

print(df2.loc["Pikachu", [" Height(m)", " Weight(kg)"]] ,end = "\n\n")

#D
#Selecting a range of rows
print(df2.loc["Pikachu" : "Sandslash", [" Height(m)", " Weight(kg)"]], end = "\n\n") #Sandslash inclusive

#E
#Using iloc 

print(df2.iloc[0:11:5, 0:4], end = "\n\n") #Last index exclusive, Pokemons from 0 to 11 at a step of 5, and first 4 (0,1,2,3) columns


##Exercise!!!
## -- Take a pokemon name as input from the user and return the pokemon info from dataset

name_pokemon = input("Enter the pokemon's name: ")

df3 = pd.read_csv(r"D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv", index_col = " Name")

print(df3.loc[name_pokemon], end = "\n\n")

### Do the same exercise by using exception handling