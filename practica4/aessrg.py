from Crypto.Cipher import AES
from Crypto.Util import Counter
 
iv = open('2015_10_01_18_57_40_gonzalo.diez.puerta_trasera.enc', 'rb').read()[:16]
 
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)

for i in range(256):
    k = [chr(ord(x)^i) for x in iv]
    k = ''.join(k)
    obj = AES.new(k, AES.MODE_CBC, iv)
    
    decr = obj.decrypt(open('2015_10_01_18_57_40_gonzalo.diez.puerta_trasera.enc','rb').read())

    last = len(decr)-1

    padding = int(toHex(decr[last]),16)

    bueno = True

    if padding > 15:
        bueno = False
    else:
        for j in range(padding,0, -1):
            # print (j, last, last-(j-padding))
            if int(toHex(decr[last+(j-padding)]),16) == padding:
                decr = decr[:-1]
            else:
                bueno = False
    # print "malo ", i
    if bueno:
        open('resultados/'+str(i)+'.txt', 'wb').write(decr)