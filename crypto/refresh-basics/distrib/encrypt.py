from Crypto.Util.number import *

flag = b'<redacted>'
flag = bytes_to_long(flag)

p = getPrime(64)
q = getPrime(256)
n = p * q

assert n > flag

l = (p-1) * (q-1)

e = 65535
d = pow(n, e, -1)

ct = pow(flag, e, n)

print("n:", n) # 1611913360955528663054324169736689343135929083519085238380892808738256415602840059371434432090673
print("ct:", ct) # 958641319547732447747427478465970976236954956070767518975162742968210412550503669031432234762485