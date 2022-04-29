#!/usr/bin/python

G = 10
H = 15

def pad(a, size):
   return [i * 2 ** (size - i.bit_length()) for i in a]

def G_hash(r):
    return pad(r, G)

def H_hash(x):
    return pad(x, H)

def xor(a, b):
    assert len(a) == len(b)
    return [a[i] ^ b[i] for i in range(len(a))]

def encrypt_key(m1, r):
    x = xor(pad(m1, G), G_hash(r))
    y = xor(pad(r, H), H_hash(x))
    return x+y

def stoi(s):
    return [ord(c) for c in s]

def itos(a):
    return ''.join(chr(i) for i in a)

m1 = 'mamamama'
r = 'maglione'

b_m1 = stoi(m1)
b_r = stoi(r)

b_key = encrypt_key(b_m1, b_r)

print([b.bit_length() for b in b_key])
print(itos(b_key).encode('utf-8'))
