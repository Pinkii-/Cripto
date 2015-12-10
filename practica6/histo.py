from Crypto.Hash import SHA512
import matplotlib.pyplot as plt

def toggleBit(number, bit):
	mask = (1 << bit)
	return (number ^ mask)

def testBit(number, bit):
	mask = 1 << bit
	return (number & mask)


i = 4222864395

k = hex(i).replace('0x','').replace('L','')
entrada = '0'*(128-len(k)) + k
m = SHA512.new(entrada)
finalHash = m.hexdigest()

nCambios = [0]*(512)
cPosicion = [0]*(512)

for x in range(512):
	newEntrada = toggleBit(int(entrada,16),x)
	mx = SHA512.new(hex(newEntrada).replace('0x','').replace('L',''))

	hashx = mx.hexdigest();

	cambios = 0

	for index in range(512):
		if (testBit(int(finalHash,16),index) and not testBit(int(hashx,16),index)) or (not testBit(int(finalHash,16),index) and testBit(int(hashx,16),index)):
			cPosicion[index] += 1
			cambios += 1

	nCambios[cambios] += 1


y = [x for x in range(512)]
xx = y
ax = plt.subplot(111)
ax.bar(xx,nCambios, width=1)

plt.axis([0,512, 0, max(nCambios)*1.1])

plt.xlabel('Numero de bits que cambian')
plt.ylabel('Numero de veces que ha cambiado')
plt.title(r'Numero de bits de cambian al cambiar un bit')

plt.savefig('1.png')

plt.close()
ax1 = plt.subplot(111)
ax1.bar(xx,cPosicion, width=1)

plt.axis([0,512, 0, max(cPosicion)*1.1])

plt.xlabel('Numero de bit')
plt.ylabel('Numero de veces que ha cambiado')
plt.title(r'Numero de veces que cambia cada bit')

plt.savefig('2.png')
plt.close()
nCambios = [0]*(512)
cPosicion = [0]*(512)

for x in range(512):
	for y in range(x,512):
		newEntrada = toggleBit(int(entrada,16),x)
		newEntrada = toggleBit(newEntrada,y)

		mx = SHA512.new(hex(newEntrada).replace('0x','').replace('L',''))

		hashx = mx.hexdigest();

		cambios = 0

		for index in range(512):
			if (testBit(int(finalHash,16),index) and not testBit(int(hashx,16),index)) or (not testBit(int(finalHash,16),index) and testBit(int(hashx,16),index)):
				cPosicion[index] += 1
				cambios += 1

		nCambios[cambios] += 1


print nCambios

print cPosicion



y = [x for x in range(512)]
xx = y
ax2 = plt.subplot(111)
ax2.bar(xx,nCambios, width=1)
plt.xlabel('Numero de bits que cambian')
plt.ylabel('Numero de veces que ha cambiado')
plt.title(r'Numero de bits de cambian al cambiar dos bits')

plt.axis([0,512, 0, max(nCambios)*1.1])

plt.savefig('3.png')
plt.close()

ax3 = plt.subplot(111)
ax3.bar(xx,cPosicion, width=1)

plt.axis([0,512, 0, max(cPosicion)*1.1])

plt.xlabel('Numero de bit')
plt.ylabel('Numero de veces que ha cambiado')
plt.title(r'Numero de veces que cambia cada bit')
plt.savefig('4.png')

