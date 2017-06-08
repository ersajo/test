import numpy
import time
perReduccion = [45, 21, 60, 12, 23, 49, 33,  5,
                62, 57,  3, 38,  1, 19, 54,  9,
                15, 20,  7, 50, 43 , 4, 46, 31,
                58, 36, 53, 22, 41, 35, 29, 55,
                27, 14, 44, 63,  6, 51, 34, 11,
                42, 28, 61, 17, 13, 37, 52, 30,
                10, 39, 25,  2, 59, 18, 26, 47]

perConcatenate1 = [30, 52,  7, 19, 39, 55, 28, 13,
                    4, 18, 53, 29, 47,  9, 32,  6,
                   43, 24, 40, 17, 50,  2, 15,  1,
                    5, 27, 54, 14, 49, 37, 38, 22,
                   31, 12, 48, 23, 33, 10, 26, 25,
                   42,  3, 41, 34,  8, 35, 51, 11]

perConcatenate2 = [37, 34, 15, 23, 48, 22, 42, 47,
                   49, 54, 43, 24, 55,  3, 35, 40,
                   19, 11, 14, 44, 10, 29, 45, 52,
                   21, 25, 31,  9, 41, 28, 33,  1,
                   13, 32,  4, 51, 17,  8, 39, 30,
                   27, 38, 20, 12,  5, 53, 50,  7]

perSecBin1 = [37, 17,  9, 10, 40, 23, 14, 18,
               3, 42, 39, 35, 15, 32, 24, 28,
              12, 22, 48, 47, 19,  7, 44, 16,
              30, 27, 20, 42, 25, 33,  2, 31,
               4, 23, 12,  5, 26, 21, 38, 43,
              41, 34,  3,  7,  1, 11, 31, 37,
               6, 36, 29, 45, 46, 13, 28, 17,
              27, 19, 11,  8,  3, 29,  1, 47]

perSecBin2 = [47,  1, 39,  2, 48, 40, 31, 11,
               9, 18,  3, 23, 21,  8, 35, 25,
              31, 14, 20, 12, 38, 37, 16, 27,
              26, 46,  7, 17, 32, 48, 10, 33,
              34, 15, 28, 22, 24,  2, 42,  5,
              23, 29, 43, 13, 41, 26, 12, 39,
              45, 27, 29, 11, 44, 30, 17,  4,
              18, 37,  1, 19,  7,  9,  6, 47]

perSecBin3 = [13, 48, 15, 29, 37, 10, 24,  5,
              11,  7, 47, 21, 12, 27,  3, 35,
              21, 41, 31, 44, 30, 19, 39, 23,
               2, 34, 17, 25, 22, 46, 36, 31,
              33, 43,  9,  4, 14, 28, 17,  4,
               7, 11,  3,  8, 32, 19, 47, 26,
              40, 23, 45, 38,  6, 12, 42,  8,
              18, 42, 37, 12,  4, 16, 20,  2]

perSecBin4 = [17,  8, 18, 38, 11, 42, 21,  1,
              19, 46, 23, 47, 31, 39, 43, 35,
              23, 28, 17, 37, 22, 45,  7, 20,
              13, 33, 15, 32,  6, 44, 29, 12,
              37, 16, 27, 26, 21,  5, 34, 36,
               9,  3, 11, 10,  2, 27, 40, 31,
              30, 15, 19, 48,  8,  3, 12,  4,
              37, 47,  1, 24,  7, 25, 14, 41]

perSecBin5 = [ 7, 22, 38, 18, 33, 26, 48, 39,
               8, 45, 28, 42, 35, 24, 32, 12,
              27, 47, 21, 13,  2,  9, 23, 42,
              46,  3, 41, 10, 14, 41, 37, 11,
              11, 34,  7, 31,  1, 27, 17,  3,
              30, 31, 36, 17, 21, 12, 19, 44,
              47, 29, 40, 38, 23, 29, 16,  4,
               5, 20,  6, 15, 43, 37,  1, 25]

perSecBin6 = [29, 35, 12, 11,  9, 41, 24, 14,
              29, 15,  1, 19, 32, 22, 18, 27,
              33, 25, 43,  1,  2, 23, 45, 31,
               5, 40, 47, 17, 38, 39, 17, 37,
              36, 21, 13,  7,  3, 16, 28, 48,
              21,  6, 31, 44, 30, 38, 10, 12,
              34,  7,  8,  4, 27, 42, 46, 26,
              42, 20, 23, 41, 11,  3, 47, 37]

perSecBin7 = [23, 36, 16, 44, 39, 12, 19,  2,
              35, 46, 33, 20,  3,  7, 29,  8,
              13, 18,  5, 14, 17, 22, 31, 47,
              34, 40, 27,  4, 48, 41, 37, 12,
              27, 31,  6, 30, 28, 43, 47, 42,
              21, 41, 23,  3, 17, 38,  1,  7,
              26, 24, 21, 42,  9, 10, 15, 45,
              32, 11,  1, 37, 38, 11, 25, 29]

perSecBin8 = [20,  1, 10, 47,  7, 29,  4, 16,
              37, 19, 35,  9, 37, 41, 44, 26,
              30, 23, 25, 15, 14,  2, 12, 11,
              14, 38, 22,  8, 38, 42, 48,  7,
              47, 46,  5, 17, 31, 39, 23, 27,
               3, 33,  6, 28, 18, 21,  1, 17,
              42, 34, 43, 41, 13, 11, 45, 29,
              36,  3, 32, 27, 21, 40, 12, 31]

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

def genSubKey(key):
    subkey = []
    for bit in perReduccion:
        subkey.append(key[bit-1])
    tempL = subkey[:28] #Mas significativos
    tempR = subkey[28:] #Menos significativos
    C = []
    for i in range(1,16):
        tempR = numpy.roll(tempR, -(1+((i-1)%2)))
        tempL = numpy.roll(tempL, -(1+((i-1)%2)))
        R = []
        L = []
        for y in range(28):
            R.append(tempR[y])
            L.append(tempL[y])
        aux = R + L
        temp = []
        if i % 2 == 0:
            for bit in perConcatenate1:
                temp.append(aux[bit-1])
        else:
            for bit in perConcatenate2:
                temp.append(aux[bit-1])
        C.append(temp)
    return C

def expandir(Num, temp):
    out = []
    if (Num == 0):
        for bit in perSecBin1:
            out.append(temp[bit-1])
    elif (Num == 1):
        for bit in perSecBin2:
            out.append(temp[bit-1])
    elif (Num == 2):
        for bit in perSecBin3:
            out.append(temp[bit-1])
    elif (Num == 3):
        for bit in perSecBin4:
            out.append(temp[bit-1])
    elif (Num == 4):
        for bit in perSecBin5:
            out.append(temp[bit-1])
    elif (Num == 5):
        for bit in perSecBin6:
            out.append(temp[bit-1])
    elif (Num == 6):
        for bit in perSecBin7:
            out.append(temp[bit-1])
    elif (Num == 7):
        for bit in perSecBin8:
            out.append(temp[bit-1])
    return out

def getSecuenciaBin(NumBits1, C, seq1, k):
    while seq1.count(1) < NumBits1:
        temp = []
        if k < 13:
            k += 1
            for i in range(48):
                aux = C[k][i] ^ C[k+1][i]
                temp.append(aux)
            seqtemp = expandir(NumBits1 % 8, temp)
            seq1 += seqtemp
        else:
            nkey = C[14] + C[13][16:32]
            nC = genSubKey(nkey)
            k = 0
            getSecuenciaBin(NumBits1, nC, seq1, k)
    return seq1

key = raw_input("Write a key>> ")
while len(key) != 8:
    key = raw_input ("Wrong key, Key must be 8 characters.\n Write another key >> ")
key = tobits(key)
C = genSubKey(key)
message = raw_input("Write a message>> ")
NumBits1 = len(message)*8
k = 0
temp = []
for i in range(48):
    aux = C[k][i] ^ C[k+1][i]
    temp.append(aux)
seq1 = expandir(NumBits1 % 8, temp)
secBin = getSecuenciaBin(NumBits1, C, seq1, k)
unos = len(message)*8
r = 0
seq2 = []
while unos > 0:
    if secBin[r] == 1:
        unos -= 1
    seq2.append(secBin[r])
    r += 1
longitud = len(seq2)
message = tobits(message)
with open('img.jpg','rb') as img:
    content = tobits(img.read())
posSeq2 = 0
posMensaje = 0
if len(seq2) <= (3*400*200):
    while longitud > 0:
        if seq2[posSeq2] == 1:
            content[ + posSeq2] = message[posMensaje]
            posMensaje += 1
        posSeq2 += 1
        longitud -= 1
longitud = len(seq2)
content = frombits(content)
for char in content:
    print ord(char)
with open('enc.jpg','wb') as enc:
    enc.write(content)
