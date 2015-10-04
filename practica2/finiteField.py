

def bit(x):
	mask = 0xff
	return x & mask

def testBit(number, bit):
	mask = 1 << bit
	return (number & mask)

def setBit(number, bit):
	mask = 1 << bit
	return (number | mask)

def clearBit(number, bit):
	mask = ~(1 << bit)
	return (number & mask)

def add1AtBit(number, bit):
	mask = (1 << bit)
	return (number ^ mask)

def getMaxBit(number):
	for i in range(15,0,-1):
		if testBit(number,i) != 0:
			return i
	return 0

def GF_mod(number, divisor):
	maxbitDiv = getMaxBit(divisor)
	for i in range(15,7,-1):
		if testBit(number,i):
			number = number ^ (divisor << (i-maxbitDiv))
	return number


def GF_product_p(a,b):
	solucion = 0x0000
	for i in range(0,8):
		if testBit(a,i) != 0:
			for j in range(0,8):
				if testBit(b,j) != 0:
					solucion = add1AtBit(solucion,i+j)
	solucion = GF_mod(solucion,0x011b)
	return solucion

def GF_tables():
	exponent = [[0x00 for i in range(0,16)] for j in range(0,16)]
	number = 0x01
	mult = 0x03
	for i in range(0,16):
		for j in range(0,16):
			if i == 0 and j == 0:
				continue
			number = GF_product_p(number,mult)
			exponent[i][j] = number

	logarit = [[0x00 for i in range(0,16)] for j in range(0,16)]
	for i in range(0,16):
		for j in range(0,16):
			ij = (i << 4) + j

			xy = exponent[i][j]
			x = xy >> 4
			y = xy & 0x0f

			logarit[x][y] = ij


	return exponent, logarit


def main():

	print(hex(GF_product_p(0x57,0x83)))
	print(bin(GF_product_p(0x57,0x83)))

	a,b=GF_tables()

	# for c in GF_tables():
	# 	for cc in c:
	# 		print (hex(cc))




if __name__ == '__main__':
	main()