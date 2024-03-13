import requests

def key_scheduling(key):
    sched = [i for i in range(0, 256)]
    
    i = 0
    for j in range(0, 256):
        i = (i + sched[j] + key[j % len(key)]) % 256
        
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
    return sched
    

def stream_generation(sched):
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (sched[i] + j) % 256
        
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
        yield sched[(sched[i] + sched[j]) % 256]        
    
def decrypt(ciphertext, key):
    ciphertext = ciphertext.split('0X')[1:]
    ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    key = [ord(char) for char in key]
    
    sched = key_scheduling(key)
    key_stream = stream_generation(sched)
    
    plaintext = ''
    for char in ciphertext:
        dec = str(chr(char ^ next(key_stream)))
        plaintext += dec
    
    return plaintext

ct = "0X290X4C0X3C0X50X570X580X990X810X230X100X670XCF0X00X400X8C0XF10X2B0X970XBC0X30XC30X590XB70X630XA30X7D0XC40XF20XCE0XF00XD50X340X40X130X720XC40X3C0X120X42"
key = "ijwZQPXEIw0lmVxSyrkIL1Oj2WXR5SJU"

requests.post("https://www.google.com/", data={"data": decrypt(ct, key)})

print("Flag sent successfully!")