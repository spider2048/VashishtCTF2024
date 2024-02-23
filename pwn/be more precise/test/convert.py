import struct

def hex_to_double(hex_str):
    binary_str = bytes.fromhex(hex_str)
    double_val = struct.unpack('!d', binary_str)[0]
    return double_val

while True:
    print(hex_to_double(input("$ ")))