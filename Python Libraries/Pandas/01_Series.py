import pandas as pd 

# print(pd.__version__) #To check version of pandas

#Series: 1 dimensional labelled array that can hold any data type
#        Its like a single labelled column in a spreadsheet (1-D)

#1-- Making a series

data1 = ["A", 101, True]

series1 = pd.Series(data1)

print(series1, end = '\n\n') #Series is displayed as a labelled column
              #By default -- the indexes are 0,1,2.. we can update them by another argument inside Series constructor(not a fn)
              #below the series, metadata(here data type is shown!!)

#If data = [100.1, 101.99, 102.0], dtype -- float64,
#If data = booleans (True/False), dtype -- bool,
#If data = 3 characters, dtype -- str!!
#If data = mix of diff data types, dtype -- object!!


#2-- Assigning indexes manually

data2 = [101, 102, 103]

series2 = pd.Series(data2, index = ["Apartment-1", "Apartment-2", "Apartment-3"])

print(series2, end = "\n\n")


#3-- Using loc property(location by label) and iloc(integer position)

print(series2.loc["Apartment-2"])

series2.loc["Apartment-3"] = 104
print(series2, end = "\n\n")

print(series2.iloc[2])

series2.iloc[2] = 103
print(series2, end = "\n\n")

#4-- Filter by value

data3 = [101, 102, 103, 201, 202]

# series3 = pd.Series(data3, index = ['a', 'b', 'c']) #This gives an error for data3

series3 = pd.Series(data3, index = ['a', 'b', 'c', 'd', 'e'])

#Printing values > 200 
print(series3[series3 > 200], end = "\n\n")

#Printing 102 with index and metadata
print(series3[series3 == 102], end = "\n\n")

#5-- Using dictionary as data instead of list..abs

data4 = {1 : "Pikachu", 2 : "Bulbasaur", 3 : "CharLizard", 4 : "PsyDuck"}

series4 = pd.Series(data4)

print(series4, end = "\n\n")

#NOTE::(IMPORTANT)

# data5 = {1 : "Pikachu", 2 : "Bulbasaur", 3 : "CharLizard", 4 : "PsyDuck"}

# series5 = pd.Series(data5, index = ["Pokemon1", "Pokemon2"])

# print(series5, end = "\n\n")

##The code above doesnt give output as intended.
##For dictionaries, The keys provided with dictionary are used as ultimate truth in pandas
##What we put as index in pd.Seres, is something which python looks for in dict, but since it couldnt find it, it returns NaN
