import pandas as pd 

#Filtering-- Keeping the rows that match a condition

df = pd.read_csv(r"D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv", index_col = " Name")

#Removing spaces in column names!!

df.columns = df.columns.str.strip()

#1-- Filter out pokemons whose weight > 150kgs and legendary pokemons from dataset

heavy_pokemon = df[df["Weight(kg)"] > 150]
print(heavy_pokemon, end = "\n\n")

legendary_pokemon = df[df["Legendary"] == True]
print(legendary_pokemon, end = "\n\n")

#2-- Filter out pokemons which are both fire and flying type

#NOTE: For python libraries dont use and(for And) , or(for Or) .. as the libraries use C style logical ops..abs
# USE -- &(for And) , |(for Or)

fire_flying_pokemon = df[(df["Type1"] == "fire") & (df["Type2"] == "flying")] #Enclose conditions in paranthesis, or
                                                                                #python interpretor might misread 
                                                                                 #and give wrong results

print(fire_flying_pokemon, end = "\n\n")