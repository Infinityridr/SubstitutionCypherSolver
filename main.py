KEY = ""
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
filename = ""


def lowDecypher(char):
	global Alphabet, KEY
	return Alphabet.lower()[KEY.lower().index(char)]

def upperDecypher(char):
	global Alphabet, KEY
	return Alphabet[KEY.index(char)]

def keyValidate():
	global KEY
	if(KEY == ""):
		KEY = "DECKFMYIQJRWTZPXGNABUSOLVH"
		return 0

	if(not(KEY.isalpha())):
		print("Key is not Letters.")
		exit()

	if(KEY.islower()):
		KEY = KEY.upper()

	return 0

def textValidate():
	global filename
	if (filename == ""):
		filename = "message.txt"

	try:
		f = open(filename,"r")
		f.close()
		
	except IOError:
		print("cannot access text file")
		exit()

	return 0

def setup():
	global KEY, filename
	output = ""

	filename = input("Name of text file to decrypt (Ex: text.txt) (same directory as program)")
	KEY = input("The decrytion key (Ex: DECKFMYIQJRWTZPXGNABUSOLVH)")

	keyValidate()
	textValidate()

def decrypt():
	global filename

	output = ""

	with open(filename,"r") as f:
		text = f.read()

	for char in text:
	
		if(not(char.isalpha())):
			output += char
			continue

		if(char.islower()):
			output += lowDecypher(char)
			continue

		output += upperDecypher(char)

	print(output)

setup()
decrypt()
