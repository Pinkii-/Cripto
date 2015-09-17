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
	import math
	global data
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
		


		if input("--- Solucion? [y/n] (clave " + str(clave) + ") ") == "y":
			print ("--------- La clave es: " + str(clave))
			break


def vigenere():
	import re
	import fractions

	global data
	global frequency
	global dataFreq

	data = re.sub('[\W_]', '', data)

	biagram = {}

	pos = -1
	for c1,c2,c3,c4,c5,c6,c7,c8,c9 in zip(data,data[1::],data[2::],data[3::], data[4::], data[5::],data[6::], data[7::],data[8::]):
		pos += 1
		bi = c1+c2+c3+c4+c5+c6+c7+c8+c9
		if not bi in biagram:
			biagram[bi] = [pos]
		else:
			biagram[bi].append(pos)

	gcds = {}
	for c in sorted(biagram, key=lambda k: len(biagram[k]), reverse=True):
		if len(c) < 3:
			break
		for ap1, ap2, ap3 in zip(biagram[c],biagram[c][1::],biagram[c][2::]):
			g = fractions.gcd(ap2-ap1,ap3-ap2)
			if g in gcds:
				gcds[g] += 1
			else:
				gcds[g] = 1

	for c in sorted(gcds, key=gcds.get, reverse=True):
		print(c,gcds[c])





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
	elif encrypt == "escitalo":
		data = open(glob.glob(filepath)[0],'r').read()
		escitalo()
	elif encrypt == "vigenere":
		vigenere()

if __name__ == '__main__':
	main()

# letras: (caracter + clave) % alfabero.lenght + 65