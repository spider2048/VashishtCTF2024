import png
import zlib

def recompute_crc(chunk_type, chunk_data):
    crc = zlib.crc32(chunk_type)
    crc = zlib.crc32(chunk_data, crc)
    crc = crc & 0xffffffff
    return crc

def extract_chunks(png_file):
    with open(png_file, 'rb') as f:
        reader = png.Reader(f)
        chunks = []
        for chunk_type, chunk_data in reader.chunks():
            crc = recompute_crc(chunk_type, chunk_data)
            chunks.append(crc)
    return chunks

png_file = 'original.png'
chunks = extract_chunks(png_file)

with open(png_file, 'rb') as fd:
    content = fd.read()

holders = [
    b'\xAA\xAA\xAA\xAA',
    b'\xBB\xBB\xBB\xBB',
    b'\xCC\xCC\xCC\xCC',
    b'\xDD\xDD\xDD\xDD'
]

for holder, crc in zip(holders, chunks):
    print("Chunk:", hex(crc))
    content = content.replace(int(crc).to_bytes(4, byteorder='big'), holder)

with open("placeholder.png", "wb+") as fd:
    fd.write(content)
