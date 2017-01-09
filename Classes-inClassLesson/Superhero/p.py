from superman import *

if __name__ == '__main__':
	jimmy_olsen = Sidekick("Jimmy Olsen")

superman = Superman()
superman.sidekicks.add(jimmy_olsen) #we added Jimmy Olsen, independent of Superman
superman.add_power("Laservision")
superman.fly() #Now I can fly
print(superman)
# or
print(dir(superman)) #see properties using dir