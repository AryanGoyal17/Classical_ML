import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv(r"D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv")

df.columns = df.columns.str.strip()

pokemon_type1 = df["Type1"].value_counts(ascending=True) #Important

plt.barh(pokemon_type1.index, pokemon_type1.values, color = "green", edgecolor = "black")

plt.title("No of pokemons of each type(Type-1)", fontweight = "bold")
plt.xlabel("No of pokemons", fontweight = "bold")
plt.ylabel("Type of pokemon", fontweight = "bold")

plt.tight_layout()
plt.show()