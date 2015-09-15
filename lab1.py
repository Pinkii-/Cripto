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

def escitalo():
	import re, math
	global data
	#data = re.sub('[\W_]', '', data)
	clave = 0
	while True:
		clave += 1
		lenght = len(data)
		count = 100
		for c in range(0,math.ceil(lenght/clave)):
			for i in range(0, clave):
				print(data[c+i*int(lenght/clave)],end="")
				count -= 1
				if count < 0:
					break
			if count < 0:
					break


		print("---")
		count = 100
		for c in range(0,clave):
			for i in range(0, math.ceil(lenght/clave)):
				print(data[i*clave+clave],end="")
				count -= 1
				if count < 0:
					break
			if count < 0:
					break
		


		if input(" Solucion? [y/n] (clave " + str(clave) + ") ") == "y":
			print ("--------- La clave es: " + str(clave))
			break

def main():
	encrypt = "";
	tipos = ["cesar","escitalo","vigenere"]
	while not encrypt in tipos:
		encrypt = input("Encriptacion? " + str(tipos) + " ")

	filepath = "./*." + encrypt.title();
	global data
	data = open(glob.glob(filepath)[0],'r').read()#.upper()

	getFreq()

	if encrypt == "cesar":
		cesar()
	elif encrypt == "escitalo":
		escitalo()

if __name__ == '__main__':
	main()

# letras: (caracter + clave) % alfabero.lenght + 65