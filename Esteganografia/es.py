permutacion = [45, 21, 60, 12, 23, 49, 33,  5,
               62, 57,  3, 38,  1, 19, 54,  9,
               15, 20,  7, 50, 43 , 4, 46, 31,
               58, 36, 53, 22, 41, 35, 29, 55,
               27, 14, 44, 63,  6, 51, 34, 11,
               42, 28, 61, 17, 13, 37, 52, 30,
               10, 39, 25,  2, 59, 18, 26, 47]

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

def genSubKey(key, permutacion):
    subkey = []
    key = tobits(key)
    for bit in permutacion:
        subkey.append(key[bit-1])
    L = subkey[:28] #Mas significativos
    R = subkey[28:] #Menos significativos
    i = 1

key = raw_input("Write a key>> ")
while len(key) != 8:
    key = raw_input ("Wrong key, Key must be 8 characters.\n Write another key >> ")
print tobits(key)
genSubKey(key, permutacion)
