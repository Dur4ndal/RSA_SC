#!/usr/bin/python
import random, secrets, string                  #A biblio "secrets" esta sendo usada APENAS para a geracao randomica de uma string para ser usada como K

                                                #10 rounds para uma chave de 128 bits de tamanho
s_box = [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]


def aesKeyGenerator():
        aesKeyLength = 16                       #16 bytes de tamanho = 128 bits de tamanho | 1 char = 1 byte
        K = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(aesKeyLength))
        return K



def matrixGenerator(chave):                     #Gera a matriz de 128 bits para texto e chave
        def Convert(string):                    #Forma elegante de split de string para cada caractere
                list1=[]
                list1[:0]=string
                return list1

        statearray = [[0 for x in range(4)] for x in range(4)]
        Convert(chave)
        x = 0
        for i in range(4):
                for j in range(4):
                        statearray[i][j] = chave[x]
                        x += 1
        return statearray


def conversaoLista2Byte(lista):
        for i in range(4):                      #str --> byte --> add na lista
                for j in range(4):
                        x = lista[i][j]
                        #x = int.from_bytes(x,"big")
                        x = ord(x)
                        lista[i][j] = x
        return lista
########################################################################################################
def addRoundKey(listaChave,listaTexto):         #Bitwise XOR entre bytes
        def bitwise_xor_bytes(a, b):
#               result_int = int.from_bytes(a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
                result_int = a ^ b
#               return result_int.to_bytes(max(len(a), len(b)), byteorder="big")
                return result_int

        for i in range(4):
                for j in range(4):
                        listaTexto[i][j] = bitwise_xor_bytes(listaChave[i][j],listaTexto[i][j])
#                       listaTexto[i][j].hex()
        return listaTexto
#######################################################################################################
def subBytes(listaRodada):
        for i in range(4):                      #byte --> int --> Pega o index na lista --> add na lista como int --> byte
                for j in range(4):
                        x = listaRodada[i][j]
                        x = s_box[x]
                        listaRodada[i][j] = x
        return listaRodada

def shiftRows(listaRodada):
        for j in range(1,4):
                for i in range(j):
                        x = listaRodada[0][j]                   #ROTATE 1,2,3 BYTE
                        listaRodada[0][j] = listaRodada[1][j]
                        listaRodada[1][j] = listaRodada[2][j]
                        listaRodada[2][j] = listaRodada[3][j]
                        listaRodada[3][j] = x
        return listaRodada

def mixColumns(a,b,c,d):
        listaVideo[i][0] = (gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1))
        listaVideo[i][1] = (gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1))
        listaVideo[i][2] = (gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3))
        listaVideo[i][3] = (gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2))

def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a

def printHex(val):
    return print('{:02x}'.format(val), end=' ')


listaVideo = [[0x19,0x3d,0xe3,0xbe],[0xa0,0xf4,0xe2,0x2b],[0x9a,0xc6,0x8d,0x2a],[0xe9,0xf8,0x48,0x08]]  #BOTAR A MATRIZ DOS ROUNDS AQUI !!!
#listaVideo = [['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','P']]
#listaVideo = conversaoLista2Byte(listaVideo)
print(listaVideo)

for i in range(4):
        for j in range(4):
                printHex(listaVideo[i][j])
print()
listaVideo = subBytes(listaVideo)
for i in range(4):
        for j in range(4):
                printHex(listaVideo[i][j])
print()

listaVideo = shiftRows(listaVideo)
for i in range(4):
        for j in range(4):
                printHex(listaVideo[i][j])
print()

for i in range(4):
        mixColumns(listaVideo[i][0],listaVideo[i][1],listaVideo[i][2],listaVideo[i][3])

for i in range(4):
        for j in range(4):
                printHex(listaVideo[i][j])
print()
#### ROUNDKEY ####
listaKey = [[0xa0,0xfa,0xfe,0x17],[0x88,0x54,0x2c,0xb1],[0x23,0xa3,0x39,0x39],[0x2a,0x6c,0x76,0x05]]
listaVideo = addRoundKey(listaKey,listaVideo)

for i in range(4):
        for j in range(4):
                printHex(listaVideo[i][j])
