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
        cifra = [pow(i,key,n) for i in textoplano]
        return cifra



def decifracao(chave, textocifrado):
        #Abertura da tupla
        key,n = chave
        #Conversao das letras cifradas baseada na chave
        return bytearray([pow(i, key, n) for i in textocifrado])

def tob64(a):
    b_a = bytearray()
    for i in a:
        ba = bytearray()
        while i:
            ba.append(i & 0xFF)
            i >>= 8
        b_a += ba
    return b_a.decode('latin-1')



