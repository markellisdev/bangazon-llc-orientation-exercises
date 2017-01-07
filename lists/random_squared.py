import random

random_numbers = [ ]

for _i in range(20):
    random_numbers.append(random.randrange(0, 49, 2))

print(random_numbers)
