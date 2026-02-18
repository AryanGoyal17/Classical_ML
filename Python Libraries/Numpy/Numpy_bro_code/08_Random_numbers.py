import numpy as np 

#Random Numbers in Numpy

##1--

#A

#rng is an object which is used to generate random numbers
rng = np.random.default_rng() 

#Random integers b/w 1-7, The second argument is exclusive like in string slicing...
print(rng.integers(1, 7))#M1
print(rng.integers(low = 1, high = 7), end = "\n\n")#M2, Here keyword arguments are used for readibility... Both methods are correct

#B

#Printing more than 1 random integer(by default 1-dimensional array created, you can change the dimension)
print(rng.integers(1, 101, size = 6), end = "\n\n")
print(rng.integers(1, 101, size = (3,2)), end = "\n\n") #3-rows, 2-columns

##2-- 

#Printing floating point numbers
#Use np.random.uniform...

print(np.random.uniform(-1, 1, size = (3,2)), end = "\n\n")


##3-- 

#Setting a seed(By using a seed, you can print the same results again and again as long as same seeed is used)

#NOTE: For integers, specifiy seed in rng = np.random.default_rng(seed = Seed-value)

#NOTE: For float,


np.random.seed(seed = 1)
print(np.random.uniform(-1, 1, size = 3), end = "\n\n") #Output when this line runs, always same due to the seed used.

##4--

#Shuffling an array

array_shuffle = np.array([1, 2, 3, 4, 5])

rng_2 = np.random.default_rng()
rng_2.shuffle(array_shuffle)
print(array_shuffle, end = "\n\n") #Original array changed

##5--

#Random choices

rng_3 = np.random.default_rng()

fruits = np.array(["Apple", "Banana", "Coconut", "Orange"])

fruit_random = rng_3.choice(fruits)
fruits_random = rng_3.choice(fruits, size = (3,3))

print(fruit_random, end = "\n\n")
print(fruits_random)

##Random numbers, random distribution, standard normal distribution, randint etc.. are present in numpy_krish_naik notebook


