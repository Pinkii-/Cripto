import glob
import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
frequency = ["E","T","A","O","I","N"]

dataFreq = {
}


def printData(data):
	for c in data:
		print(c,end="")

def getFreq():
	global data
	global dataFreq
	for c in alphabet:
		dataFreq[c] = data.count(c)

	for c in sorted(dataFreq, key=dataFreq.get, reverse=True):
		print (c, dataFreq[c])


def cesar():
	global data
	global dataFreq
	global frequency
	solucion = "n"
	for ite in sorted(dataFreq, key=dataFreq.get, reverse=True):
		
		clave = ord(ite) - ord(frequency[0])
		for cc in data:
			c = ord(cc)
			if c >= 65 and c <= 90:
				print( chr((c+clave-65)%26+65),end="")
			else:
				print(cc,end="")
		if input("Solucion? [y/n]") == "y":
			print ("--------- La clave es: " + chr(clave+65))
			break

def main():
	encrypt = "";
	tipos = ["cesar","escitalo","vigenere"]
	while not encrypt in tipos:
		encrypt = input("Encriptacion? " + str(tipos) + " ")

	filepath = "./*." + encrypt.title();
	global data
	data = open(glob.glob(filepath)[0],'r').read().upper()

	getFreq()

	if encrypt == "cesar":
		cesar()

if __name__ == '__main__':
	main()

# letras: (caracter + clave) % alfabero.lenght + 65