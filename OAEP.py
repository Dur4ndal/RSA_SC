#!/usr/bin/env python3

import secrets
import hashlib

G = 1024
H = 512

def pad(m, size):
    bit_size = len(m) * 8
    assert bit_size <= size
    ba = bytearray(m)
    for i in range(int((size - bit_size) / 8)):
        ba.append(0)
    return ba

def G_hash(r):
    g = hashlib.sha1()
    g.update(r)
    x = g.digest() #Size = 160
    rem = int(G / 8)
    if G <= 160:
        return x[:rem]
    else: #G >160 
        while len(x) < G:
            x += x
        return x[:rem]
def H_hash(x):
    h = hashlib.md5()
    h.update(x)
    y = h.digest() #Size = 128
    rem = int(H / 8)
    if H <= 128:
        return y[:rem]
    else: #H > 128 
        while len(y) < H:
            y += y
        return y[:rem]

def xor(a, b):
    assert len(bytearray(a)) == len(bytearray(b))
    return [a[i] ^ b[i] for i in range(len(a))]

def oaep_encrypt(m1): 
    b_m1 = pad(m1.encode(), G)
    b_r = bytearray(secrets.token_bytes(int(H / 8)))
    x = xor(b_m1, G_hash(b_r))
    y = xor(b_r, H_hash(bytearray(x)))
    return itos(x+y)

def oaep_decrypt(c):
    ind = int(G/8)
    x = stoi(c[:ind])
    y = stoi(c[ind:])
    r = xor(H_hash(bytearray(x)), y)
    m1 = xor(G_hash(bytearray(r)), x)
    return bytearray(m1[:16]).decode()

def stoi(s):
    return [ord(c) for c in s]

def itos(a):
    return ''.join(chr(i) for i in a)
