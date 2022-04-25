#!/usr/bin/python
from RSA import *


qtdPrimos = 1000                                        #Qtd de primos para teste de Erator Thenes
sieveEratosThenes(qtdPrimos)


p = peqGenerator()                                      #Gera 2 tuplas com chaves publicas e privadas
while True:                                             #Loop para evitar p e q iguais
        q = peqGenerator()
        if (p != q):
                break

print("P escolhido foi")
print(p)
print("Q escolhido foi")
print(q)

#Calculo de oDn
n = p*q

print("N calculado foi:")
print(n)

oDn = (p - 1)*(q - 1)

print("O(n) calculado foi:")
print(oDn)

#Calculo da chave publica E
e = eCalculator(oDn)

print("E calculado foi:")
print(e)

#Calculo da chave privada D
d = dCalculator(e,oDn)


#Chave privada e publica (d,n) e (e,n), respectivamente
chvPriv = (d,n)
chvPubl = (e,n)

print(chvPriv,chvPubl)
print("A chave publica e:")
print(chvPubl)

print("A chave privada e:")
print(chvPriv)

msg = input("Digite a mensagem:\n")
msgCifrada = cifracao(chvPubl,msg)

#print(msgCifrada)
print(" - Sua mensagem cifrada e:  ", ''.join(map(lambda x: str(x), msgCifrada)))

msgDecifrada = decifracao(chvPriv,msgCifrada)

print(msgDecifrada)

##################
print(aesKeyGenerator())
