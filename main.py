#!/usr/bin/env python3
from RSA import *
from OAEP import oaep_encrypt, oaep_decrypt
import base64
import hashlib

#Parte I: Geracao de chaves e cifra simetrica
qtdPrimos = 1000                                        #Qtd de primos para teste de Erator Thenes
sieveEratosThenes(qtdPrimos)


p = peqGenerator()                                      #Gera 2 tuplas com chaves publicas e privadas
while True:                                             #Loop para evitar p e q iguais
    q = peqGenerator()
    if (p != q):
        break
#Calculo de oDn
n = p*q
oDn = (p - 1)*(q - 1)

#Calculo da chave publica E
e = eCalculator(oDn)
#Calculo da chave privada D
d = dCalculator(e,oDn)

chvPriv = (d,n)
chvPubl = (e,n)

chvSess = aesKeyGenerator()

msg = input("Digite a mensagem:\n")
c_key = oaep_encrypt(chvSess) #Cifracao assimetrica da chave de sessao
#TODO Cifracao simetrica da mensagem AES CTR

#Parte II: Assinatura
sha3 = hashlib.sha3_256()
sha3.update(msg.encode())
msg_hash = sha3.digest()
msgCifrada = cifracao(chvPubl,msg_hash) #Calculo e cifracao de hash da mensagem

#print("Assinatura: " + tob64(msgCifrada) + '\n')

#Parte III: Verificacao

msgDecifrada = decifracao(chvPriv,msgCifrada) #Decifracao do hash da mensagem

#Testes de adulteração das mensagens
#msgCifrada.pop()
#msgDecifrada.append(0)

flg_verificado = msg_hash == msgDecifrada #Checka se assinatura bate
print('A assinatura é ', end='')
if flg_verificado:
    print('válida.')
else:
    print('inválida.')

