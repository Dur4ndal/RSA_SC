#!/usr/bin/python

from AES import aesKeyGenerator
import sys, random, math

listaprimos = []

def nBitRandom(n):
        #Retorna um numero aleatorio, com tamanho de bits escolhido
        return(random.randrange(2**(n-1)+1, 2**n-1))



def sieveEratosThenes(n):
        #Algoritmo para verificar a primalidade de um numero dentro de uma lista de tamanho O(n)
        primo = [True for i in range(n+1)]
        p = 2
        while (p*p <= n):
                if (primo[p] == True):
                        for i in range(p*p,n+1,p):
                                primo[i] = False
                p += 1
        #Loop passando da lista de O(n) para uma lista APENAS com numeros primos
        for p in range(2,n+1):
                if primo[p]:
                        listaprimos.append(p)



def numeroPrimoLow(n):
        #Gera numeros primos candidatos para o teste de high priority, apos passar o de low priority
        while True:
                cand = nBitRandom(n)

                #Divisao pelos primeiros numeros primos calculados pelo sieveEratosThenes
                for divisor in listaprimos:
                        if cand % divisor == 0 and divisor**2 <= cand:
                                break
                else:
                        return cand



def highPriorityTest(n):
        #Teste para os candidatos a serem primos, com abordagem probabilistica
        numeroMaxDivisoesP2 = 0
        ec = n-1
        while ec % 2 == 0:
                ec >>=1
                numeroMaxDivisoesP2 += 1
        assert(2**numeroMaxDivisoesP2 * ec == n-1)

        def funcParaRodada(testador):
                if pow(testador,ec,n) == 1:
                        return False
                for i in range(numeroMaxDivisoesP2):
                        if pow(testador,2**i*ec,n) == n-1:
                                return False
                return True

        #Numero de rodadas para verificacao
        nRodadas = 20
        for i in range(nRodadas):
                testador = random.randrange(2, n)
                if funcParaRodada(testador):
                        return False
        return True



def peqGenerator():
        #Calcula P e Q
        while True:
                tamanhoBits = 1024 #Tamanho de P e Q em BITS
                candidato = numeroPrimoLow(tamanhoBits)
                if not highPriorityTest(candidato):
                        continue
                else:
                        return candidato



def eCalculator(oDn):
        #Calcula o expoente E para Chave PUBLICA
        #Escolhe aleatoriamente um numero que seja 1 < E < o(N) e se o MDC(e,oDn) == 1, ele e um e valido. Pois ambos sao COPRIMOS !
        while True:
                e = random.randrange(1,oDn)
                if ((math.gcd(e,oDn)) == 1):
                        #print(e)
                        return e



def dCalculator(e, oDn):
        #Bruxaria realizada durante a madrugada, apenas eu (Dur4ndal) e Jesus cristo sabemos o que rolou aqui. #Shalom
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        tmp = oDn

        while e>0:
                tmp1 = tmp//e
                tmp2 = tmp - tmp1*e
                tmp = e
                e = tmp2

                x = x2 - tmp1 * x1
                y = d - tmp1 * y1

                x2 = x1
                x1 = x
                d = y1
                y1 = y
        if tmp == 1:
                return d+oDn



def cifracao(chave, textoplano):
        #Abertura da tupla
        key,n = chave
        #Conversao por a^b mod m
        cifra = [pow(ord(char),key,n) for char in textoplano]
        return cifra



def decifracao(chave, textocifrado):
        #Abertura da tupla
        key,n = chave
        #Conversao das letras cifradas baseada na chave
        tmp = [str(pow(char,key,n)) for char in textocifrado]
        textoplano = [chr(int(char2)) for char2 in tmp]
        return ''.join(textoplano)


################################ main ####################################
#Quantidade de primos desejados para o teste de baixo primo
#qtdPrimos = 1000
#sieveEratosThenes(qtdPrimos)

#Gerando chave publica ---> ARRUMAR AQUI PARA P e Q NUNCA SEREM IGUAIS !!!!!!!!!!!!!!!
#p = peqGenerator()
#q = peqGenerator()

#print("P escolhido foi")
#print(p)
#print("Q escolhido foi")
#print(q)
#Calculo de oDn
#n = p*q

#print("N calculado foi:")
#print(n)

#oDn = (p - 1)*(q - 1)

#print("O(n) calculado foi:")
#print(oDn)

#Calculo da chave publica E
#e = eCalculator(oDn)

#print("E calculado foi:")
#print(e)

#Calculo da chave privada D
#d = dCalculator(e,oDn)


#Chave privada e publica (d,n) e (e,n), respectivamente
#chvPriv = (d,n)
#chvPubl = (e,n)

#print(chvPriv,chvPubl)
#print("A chave publica e:")
#print(chvPubl)

#print("A chave privada e:")
#print(chvPriv)

#msg = input("Digite a mensagem:\n")
#msgCifrada = cifracao(chvPubl,msg)

#print(msgCifrada)
#print(" - Sua mensagem cifrada e:  ", ''.join(map(lambda x: str(x), msgCifrada)))

#msgDecifrada = decifracao(chvPriv,msgCifrada)

#print(msgDecifrada)

##################
#print(aesKeyGenerator())
