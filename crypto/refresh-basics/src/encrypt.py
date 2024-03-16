from Crypto.Util.number import *

flag = b'SURGE{1e222ae77cde0b8e69bf5ce303680a69}'
flag = bytes_to_long(flag)

p = getPrime(64)
q = getPrime(256)
n = p * q

assert n > flag

e = 65537

ct = pow(flag, e, n)

print("n:", n)
print("ct:", ct)