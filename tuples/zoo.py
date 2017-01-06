zoo = ("Lion", "Tiger", "Monkey", "Turtle")
# Get animal at certain index
print(zoo[0])

for animal in zoo:
	if animal == "Lion":
		print("There's a " + animal + " in your zoo!")

# Convert tuple into a list
zooList = list(zoo)
print(zooList)

# Adding items to list- use extend
zooList.extend(["Bear", "Elephant", "Flamingo"])
print(zooList)

# Converting list to tuple
zoo = tuple(zooList)
print(zoo)

