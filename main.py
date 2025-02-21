def lowDecypher(char):
	return Alphabet.lower()[AKEY.lower().index(char)]

def upperDecypher(char):
	return Alphabet[AKEY.index(char)]

text = open("message.txt",'r').read()
output = ""

AKEY 	 = "DECKFMYIQJRWTZPXGNABUSOLVH" #PLACE THE ENCRYPTED ALPHABET HERE
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in text:
	
	if(not(char.isalpha())):
		output += char
		continue

	if(char.islower()):
		output += lowDecypher(char)
		continue

	output += upperDecypher(char)

print(output)
