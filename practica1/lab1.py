import glob
import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
frequency = ["E","T","A","O","I","N"]

dataFreq = {
}

solucion = ""

clave = 0
claveStr = ""

def printToFile(data,key,extension):
	name = "GonzaloDiezGarrido"
	filename = name + '_' + key + '.' + extension
	f = open("soluciones/"+filename,'w+')
	f.write(data)

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
	print ("")


def cesar():
	global data
	global dataFreq
	global frequency
	global solucion
	global clave
	for ite in sorted(dataFreq, key=dataFreq.get, reverse=True):
		clave = ord(ite) - ord(frequency[0])
		for cc in data:
			c = ord(cc)
			if c >= 65 and c <= 90:
				ch =chr((c+clave-65)%26+65)
				solucion+=ch
				print( ch,end="")
			else:
				solucion+=cc
				print(cc,end="")
		if input("Solucion? [y/n]") == "y":
			claveStr = chr(clave+65)
			print ("--------- La clave es: " + chr(clave+65))
			printToFile(solucion,claveStr,"Cesar")
			break

def getCesar(data):
	global frequency
	freq = {}
	for c in alphabet:
		freq[c] = data.count(c)
	for c in sorted(freq, key=freq.get, reverse=True):
		clave = c
		break
	return ord(clave) - ord(frequency[0])

def escitalo():
	import math
	global data
	global clave
	global solucion
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
				print(data[i*clave+c],end="")
				count -= 1
				if count < 0:
					break
			if count < 0:
					break
		


		if input("--- Solucion? [y/n] (clave " + str(clave) + ") ") == "y":
			print ("--------- La clave es: " + str(clave))
			claveStr = str(clave)
			for c in range(0,clave):
				for i in range(0, math.ceil(lenght/clave)):
					if i*clave+clave <= lenght:
						solucion += data[clave * i + c]
						print(data[clave * i + c],end="")
			printToFile(solucion,claveStr,"Escitalo")
			break


def vigenere():
	import re
	import fractions

	global data
	global frequency
	global dataFreq
	global solucion

	originalData = data
	data = re.sub('[\W_]', '', data)

	biagram = {}

	pos = -1
	#for c1,c2,c3,c4,c5,c6,c7,c8,c9 in zip(data,data[1::],data[2::],data[3::], data[4::], data[5::],data[6::], data[7::],data[8::]):
	for c1,c2,c3,c4,c5,c6,c7 in zip(data,data[1::],data[2::],data[3::], data[4::], data[5::],data[6::]):
		pos += 1
		#bi = c1+c2+c3+c4+c5+c6+c7+c8+c9
		bi = c1+c2+c3+c4+c5+c6+c7
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

	gcd = next(iter (gcds.keys()))
	for c in sorted(gcds, key=gcds.get, reverse=True):
		print(c,gcds[c])
		gcd = fractions.gcd(gcd,c)

	print("El gdc es " + str(gcd))

	while True:
		if not input("Te gusta la longitud de clave " + str(gcd) + "? [y/n] ") == "y":
			longitud = int(input("Introduce la longitud de la clave a probar "))
		else:
			longitud = gcd
		print ("Vamos a probar con claves de longitud " + str(longitud))

		datas = [""]*longitud
		i = 0;
		for c in originalData:
			if c >= 'A' and c <= 'Z':
				datas[i] += c
				i = (i + 1)%longitud
		
		clavesCesar = [int]*longitud
		for n in range(0, longitud):
			clavesCesar[n] = getCesar(datas[n])

		clave = ""
		for n in clavesCesar:
			clave += chr(n+65)
			print (chr(n+65),end="")
		print("")

		i = 0
		j = 0
		for c in originalData:
			if c >= 'A' and c <= 'Z':
				print (chr((ord(datas[i][j])-clavesCesar[i]-65)%26+65),end="")
				solucion += chr((ord(datas[i][j])-clavesCesar[i]-65)%26+65)
				i += 1
				if i >= longitud:
					i = 0
					j += 1
			else:
				print(c,end="")
				solucion += c

		if input("Esta bien descifrado? [y/n] ") == "y":
			print("la clave es: " + clave)
			printToFile(solucion,clave,"Vigenere")
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
	elif encrypt == "escitalo":
		data = open(glob.glob(filepath)[0],'r').read()
		escitalo()
	elif encrypt == "vigenere":
		vigenere()

if __name__ == '__main__':
	main()

# letras: (caracter + clave) % alfabero.lenght + 65
