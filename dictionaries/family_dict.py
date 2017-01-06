my_family = {'son': {'name': "Kahnu", 'age': "6"}, 'mother': {'name': 'BiBi', 'age': '82'}, 'wife': {'name': 'Jami', 'age': '46'}}



print("{0} is my {1} and is {2} years old.".format(y['name'], x, y['age']) for (x, y) in my_family.items())

# [
#   print("{0} is my {1} and is {2} years old.".format(y['name'], x, y['age']))
#   for (x, y) in my_family.items()
# ]
