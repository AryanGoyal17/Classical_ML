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
