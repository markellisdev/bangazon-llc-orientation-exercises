#song set
songs = {
	("Nickelback", "How You Remind Me"),
	("Foxy Shazam", "I Like It"),
	("Heart", "Barracuda"),
	("Tal Farlow", "Everything I've Got"),
	("Nickelback", "Animals")
}

#set comprehension {desired action or result, for key, value in set when(if) key is not equal to ""}
better_songs = {x: y for x, y in songs if x != "Nickelback"}

print(better_songs)

