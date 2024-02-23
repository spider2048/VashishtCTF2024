KEY = bytes.fromhex('7d8bc6d0e2d2525cdd68683e1330bba7') # Xor key
# 7d8bc6d0e2d2525cdd68683e1330bba7

with open("placeholder.png", "rb") as fd:
    content = fd.read()

content = content.replace(b'\xAA\xAA\xAA\xAA', KEY[ :4])
content = content.replace(b'\xBB\xBB\xBB\xBB', KEY[4:8])
content = content.replace(b'\xCC\xCC\xCC\xCC', KEY[8:12])
content = content.replace(b'\xDD\xDD\xDD\xDD', KEY[12:16])

with open("../distrib/distrib.png", "wb+") as fd:
    fd.write(content)