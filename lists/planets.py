planet_list = ["Mercury", "Mars"]
#append adds to list
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

#extend adds list to existing list
planet_list.extend(["Uranus", "Neptune"])
print(planet_list)

#insert places new planets in list at index
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
print(planet_list)

planet_list.append("Pluto")
print(planet_list)

#This slices rocky planets from the list, index position to index position
rocky_planets = planet_list[0:4]
print(rocky_planets)
print(planet_list)

#This deletes an item at this index
del(planet_list[8])
print(planet_list)

missions = [("Cassini", "Jupiter"),("Venera 10", "Venus"),("Viking 1", "Mars")]

#loop over array
for planet in planet_list:
	print(planet)

for planet in planet_list:
	for spacecraft in missions:
		if spacecraft[1] == planet:
			print("The spacecraft " + spacecraft[0] + " visited " + planet + ".")