import random

# Declared a list
random_numbers = [ ]

# Basic for loop to  create 20 random numbers using randrange
for _i in range(20):
    random_numbers.append(random.randrange(0, 49, 2))

print(random_numbers)

#Use list comprehension to build a new list containing each number squared
squared_numbers = [x**2 for x in random_numbers]
print(squared_numbers)
