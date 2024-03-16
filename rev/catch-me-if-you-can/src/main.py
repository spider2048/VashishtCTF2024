import requests
import base64


def KSC(key):
    sched = [i for i in range(0, 256)]

    i = 0
    for j in range(0, 256):
        i = (i + sched[j] + key[j % len(key)]) % 256

        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp

    return sched


def STG(sched):
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (sched[i] + j) % 256

        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp

        yield sched[(sched[i] + sched[j]) % 256]


def DC(ciphertext, key):
    # ciphertext = ciphertext.split('0X')[1:]
    # ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    # key = [ord(char) for char in key

    sched = KSC(key)
    key_stream = STG(sched)

    plaintext = ""
    for char in ciphertext:
        dec = str(chr(char ^ next(key_stream)))
        plaintext += dec

    return plaintext

ct = [41, 76, 60, 5, 87, 88, 153, 129, 35, 16, 103, 207, 0, 64, 140, 241, 43, 151, 188, 3, 195, 89, 183, 99, 163, 125, 196, 242, 206, 240, 213, 52, 4, 19, 114, 196, 60, 18, 66]
key = base64.b32decode("NFVHOWSRKBMEKSLXGBWG2VTYKN4XE22JJQYU62RSK5MFENKTJJKQ====")
print(DC(ct, key))
requests.post("https://www.google.com/", data={"data": DC(ct, key)})

print("Flag sent successfully!")
