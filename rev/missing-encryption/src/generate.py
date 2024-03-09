from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii


FLAG = b"SURGE{86b99a57986383aed0f1c3d88a1daf6c}"

key = binascii.unhexlify("cdd2e040cf21d70c4ad47a4b1a401445") # cdd2e040cf21d70c4ad47a4b1a401445
iv = binascii.unhexlify("d36c1f7aa04f1b98ca91e159f71ba68e") # d36c1f7aa04f1b98ca91e159f71ba68e

aes = AES.new(key, AES.MODE_CBC, iv)
encrypted = aes.encrypt(pad(FLAG, AES.block_size))

print("key =", binascii.hexlify(key))

iv2 = []
for ch in iv:
    iv2.append(ch ^ 0xc3)
print(iv2)
iv2 = bytearray(iv2)

print("iv2 =", binascii.hexlify(iv2))
print("encrypted =", binascii.hexlify(encrypted))

aes = AES.new(key, AES.MODE_CBC, iv)
print(aes.decrypt(encrypted))
