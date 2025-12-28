BASE64_ALPHABET = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789+/"
)


BASE64_INDEX = {c: i for i, c in enumerate(BASE64_ALPHABET)}


def base64_decode(encoded: str) -> bytes:
    decoded = bytearray()

    # 4文字ずつ処理
    for i in range(0, len(encoded), 4):
        block = encoded[i:i+4]
        padding = block.count("=")

        # '=' を 0 に置換して処理
        block = block.rstrip("=") + "A" * padding

        twenty_four_bits = 0
        for c in block:
            twenty_four_bits = (twenty_four_bits << 6) | BASE64_INDEX[c]

        # 24bit → 3バイト
        for shift in (16, 8, 0):
            decoded.append((twenty_four_bits >> shift) & 0xFF)

        # パディング分のバイトを削除
        if padding:
            decoded = decoded[:-padding]

    return bytes(decoded)

import base64

decode = base64.b64encode("hello world".encode("utf-8"))
print(decode)

print(base64_decode(decode.decode("utf-8")))

