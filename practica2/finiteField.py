import time
exponent = [[0x00 for i in range(0,16)] for j in range(0,16)]
logarit = [[0x00 for i in range(0,16)] for j in range(0,16)]

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
	global exponent, logarit
	exponent = [[0x01 for i in range(0,16)] for j in range(0,16)]
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


	# return exponent, logarit

def getXnY(n):
	return n >> 4, n & 0x0f

def GF_product_t(n1,n2):
	global exponent,logarit
	if n1 == 0 or n2 == 0:
		return 0

	x1, y1 = getXnY(n1)
	x2, y2 = getXnY(n2)

	log1 = logarit[x1][y1]
	log2 = logarit[x2][y2]

	logsol = (log1+log2)%256

	x,y = getXnY(logsol)

	return exponent[x][y]
	

def xtime(number):
	number = number << 1
	if (testBit(number,8) != 0):
		number = clearBit(number,8)
		number = number ^ 0x1b
	return number

# for x in range(1):
# 	a = xtime(a)

def GF_product_p_02(a):
	return xtime(a)

def GF_product_p_03(a):
	return a ^ xtime(a)

def GF_product_p_09(a):
	original = a
	for x in range(3):
		a = xtime(a)
	return original ^ a

def GF_product_p_0B(a):
	original = a
	a8 = a
	for x in range(3):
		a8 = xtime(a8)
	a2 = xtime(a)
	return original ^ a8 ^ a2

def GF_product_p_0D(a):
	original = a
	a8 = a
	for x in range(3):
		a8 = xtime(a8)
	a4 = a
	for x in range(2):
		a4 = xtime(a4)
	return original ^ a8 ^ a4

def GF_product_p_0E(a):
	a2 = xtime(a)
	a8 = a
	for x in range(3):
		a8 = xtime(a8)
	a4 = a
	for x in range(2):
		a4 = xtime(a4)
	return a8 ^ a4 ^ a2


def GF_product_t_02(a):
	if a == 0:
		return 0x00

	x1, y1 = getXnY(a)

	log1 = logarit[x1][y1]
	log2 = 0x19 # logarit[0][2]

	logsol = (log1+log2)%256

	x,y = getXnY(logsol)

	return exponent[x][y]


def GF_product_t_03(a):
	if a == 0:
		return 0x00

	x1, y1 = getXnY(a)

	log1 = logarit[x1][y1]
	log2 = 0x01 # logarit[0][3]

	logsol = (log1+log2)%256

	x,y = getXnY(logsol)

	return exponent[x][y]

def GF_product_t_09(a):
	if a == 0:
		return 0x00

	x1, y1 = getXnY(a)

	log1 = logarit[x1][y1]
	log2 = 0xc7 # logarit[0][9]

	logsol = (log1+log2)%256

	x,y = getXnY(logsol)

	return exponent[x][y]

def GF_product_t_0B(a):
	if a == 0:
		return 0x00

	x1, y1 = getXnY(a)

	log1 = logarit[x1][y1]
	log2 = 0x68 # logarit[0][0xB]

	logsol = (log1+log2)%256

	x,y = getXnY(logsol)

	return exponent[x][y]

def GF_product_t_0D(a):
	if a == 0:
		return 0x00

	x1, y1 = getXnY(a)

	log1 = logarit[x1][y1]
	log2 = 0xee # logarit[0][0xD]

	logsol = (log1+log2)%256

	x,y = getXnY(logsol)

	return exponent[x][y]

def GF_product_t_0E(a):
	if a == 0:
		return 0x00

	x1, y1 = getXnY(a)

	log1 = logarit[x1][y1]
	log2 = 0xdf # logarit[0][0xE]

	logsol = (log1+log2)%256

	x,y = getXnY(logsol)

	return exponent[x][y]




# shift left, if b8 == 1, xor with 0x1b


def GF_invers(a):
	global exponent,logarit
	x,y = getXnY(a)

	pos = logarit[x][y]

	thing = (255 - pos) 

	i,j = getXnY(thing)

	return exponent[i][j]



def main():
	GF_tables()
	# for x in range(500000):
		# GF_product_p(0x57,0x02)
		# GF_product_t(0x57,0x02)
		# GF_product_t_02(0x57)
		# GF_product_p(0x57,0x0D)
		# GF_product_p_0D(0x57)

	#print(hex(GF_product_t(0xA0,0xb1)))

	# print(hex(GF_mod(0xffa0,0x11b)))
	# print(hex(logarit[0][0xE]))

	stime = time.time()
	for x in range(1000000):
		GF_product_t(x%256,0x02)
	print ("t*0x02 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t_02(x%256)
	print ("t_0x02 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t(x%256,0x03)
	print ("t*0x03 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t_03(x%256)
	print ("t_0x03 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t(x%256,0x09)
	print ("t*0x09 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t_09(x%256)
	print ("t_0x09 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t(x%256,0x0B)
	print ("t*0x0B -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t_0B(x%256)
	print ("t_0x0B -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t(x%256,0x0D)
	print ("t*0x0D -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t_0D(x%256)
	print ("t_0x0D -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t(x%256,0x0E)
	print ("t*0x0E -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t_0E(x%256)
	print ("t_0x0E -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_t(x%256,x%255)
	print ("t_0 -> "+str(time.time()-stime))

	stime = time.time()
	for x in range(1000000):
		GF_product_t(x%256,0x02)
	print ("t*0x02 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p_02(x%256)
	print ("p_0x02 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p(x%256,0x03)
	print ("p*0x03 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p_03(x%256)
	print ("p_0x03 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p(x%256,0x09)
	print ("p*0x09 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p_09(x%256)
	print ("p_0x09 -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p(x%256,0x0B)
	print ("p*0x0B -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p_0B(x%256)
	print ("p_0x0B -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p(x%256,0x0D)
	print ("p*0x0D -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p_0D(x%256)
	print ("p_0x0D -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p(x%256,0x0E)
	print ("p*0x0E -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p_0E(x%256)
	print ("p_0x0E -> "+str(time.time()-stime))

	stime = time.time()	
	for x in range(1000000):
		GF_product_p(x%256,x%255)
	print ("p_0 -> "+str(time.time()-stime))

	
	# print(hex(GF_product_p(0x57,0x02)))
	# print(hex(GF_product_t(0x57,0x02)))
	# print(hex(GF_product_t_02(0x57)))
	# print(hex(GF_product_p(0x57,0x83)))
	# print(hex(GF_product_t(0x57,0x83)))

	# print(hex(GF_invers(0x05)))

	# # for c in GF_tables():
	# # 	for cc in c:
	# # 		print (hex(cc))

	# print(hex(GF_invers(GF_invers(0x03))))




if __name__ == '__main__':
	main()