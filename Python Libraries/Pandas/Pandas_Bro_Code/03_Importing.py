import pandas as pd 

#Importing CSV and JSON files using Pandas..abs

#CSV-- Comma-Separated values
#JSON-- JavaScript Object notation

#1-- Reading a CSV file

df1 = pd.read_csv("D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv")

# NOTE: The  file extension ("D:\ML_krish_naik\Data-Sets\FirstGenPokemon.csv") gives a warning -- "\M" is an invalid escape sequence

# To fix this M1-- use / instead of \, M2-- use \\ instead of \
#             M3-- use the raw string method..Put a lowercase r right outside the front quote of your string. 
#                  This tells Python, "Treat this as a raw string of text, do not look for any special slash commands."

print(df1, end = "\n\n")

#2-- Reading a JSON file

df2 = pd.read_json(r"D:\ML_krish_naik\Data-Sets\FirstGenPokemon.json")
print(df2, end = "\n\n")


#3-- Reading the full dataset!!

# When we read a CSV or JSON file using pandas, it prints first 5 and last 5 rows if to_string method not used

print(df1.to_string(), end = "\n\n") #Full dataset printed, same will work for df2
#Running this in VSCODE might not give a good output as on using to-string, we tell vscode to print(everything) in dataset..
#On using tostring vs code is not smart enough to fit the 35columns in terminal so it moves to next line on running out of space..

#NOTE: Notice the column headings when to string was not used...Try doing this in jupyter notebook, there it will work correctly