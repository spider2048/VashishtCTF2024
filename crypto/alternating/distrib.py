from Crypto.Util.number import getPrime, bytes_to_long

def SUS(num1, num2):
    bin_num1 = bin(num1)[2:]
    bin_num2 = bin(num2)[2:]

    max_len = max(len(bin_num1), len(bin_num2))
    bin_num1 = bin_num1.zfill(max_len)
    bin_num2 = bin_num2.zfill(max_len)

    result = ''
    for bit1, bit2 in zip(bin_num1, bin_num2):
        result += bit1 + bit2

    return int(result, 2)

p = getPrime(256)
q = getPrime(256)

n = p * q
e = 65535

m_ = b'<redacted>'
m = bytes_to_long(m_)

assert n > m

ct = pow(m, e, n)

print(ct) # 5151974923770453459134626360131153163601747034483452979083127819273396704515286958405343794790816219315578940696350184833498181051962056137670140243692388
print(SUS(p, q)) # 12458784209151011255873225878376042809845043197978416046632842270153209293622290894770167385050845288292259931715943485313638151930231374531212000736945971