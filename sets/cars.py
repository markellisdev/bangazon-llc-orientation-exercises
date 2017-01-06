showroom = set()
showroom.add("Tesla")
showroom.add("MINI John Cooper Works")
showroom.add("Gremlin")
showroom.add("Porsche 911")
print(len(showroom))

#Add an item twice? YES
showroom.add("Tesla")
print(showroom)

#
showroom.update({"Cutlass", "Jeep" })
print(showroom)

showroom.discard("Cutlass")
print(showroom)

junkyard = set()
junkyard.add("Pinto")
junkyard.update({"Tahoe", "Chevette", "Gremlin", "Jeep"})
same_in_both = set(showroom).intersection(junkyard)
print(same_in_both)
print(junkyard)

junkyard ^= set(showroom)
print(junkyard)

