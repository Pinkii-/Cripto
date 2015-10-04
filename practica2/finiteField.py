

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

def GF_product_p(a,b):
	solucion = 0x0000
	pass


def main():
	print(GF_product_p(0x57,0xc1))

	pass



if __name__ == '__main__':
	main()