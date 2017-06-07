import numpy
per1 = [45, 21, 60, 12, 23, 49, 33,  5,
        62, 57,  3, 38,  1, 19, 54,  9,
        15, 20,  7, 50, 43 , 4, 46, 31,
        58, 36, 53, 22, 41, 35, 29, 55,
        27, 14, 44, 63,  6, 51, 34, 11,
        42, 28, 61, 17, 13, 37, 52, 30,
        10, 39, 25,  2, 59, 18, 26, 47]

per2 = [30, 52,  7, 19, 39, 55, 28, 13,
         4, 18, 53, 29, 47,  9, 32,  6,
        43, 24, 40, 17, 50,  2, 15,  1,
         5, 27, 54, 14, 49, 37, 38, 22,
        31, 12, 48, 23, 33, 10, 26, 25,
        42,  3, 41, 34,  8, 35, 51, 11]

per3 = [37, 34, 15, 23, 48, 22, 42, 47,
        49, 54, 43, 24, 55,  3, 35, 40,
        19, 11, 14, 44, 10, 29, 45, 52,
        21, 25, 31,  9, 41, 28, 33,  1,
        13, 32,  4, 51, 17,  8, 39, 30,
        27, 38, 20, 12,  5, 53, 50,  7]

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def genSubKey(key, per1):
    subkey = []
    key = tobits(key)
    for bit in per1:
        subkey.append(key[bit-1])
    tempL = subkey[:28] #Mas significativos
    tempR = subkey[28:] #Menos significativos
    i = 1
    C = []
    for i in range(1,16):
        tempR = numpy.roll(tempR, -(1+((i-1)%2)))
        tempL = numpy.roll(tempL, -(1+((i-1)%2)))
        print tempL
        R = []
        L = []
        for y in range(28):
            R.append(tempR[y])
        for x in range(28):
            L.append(tempL[x])
    print L

key = raw_input("Write a key>> ")
while len(key) != 8:
    key = raw_input ("Wrong key, Key must be 8 characters.\n Write another key >> ")
genSubKey(key, per1)
