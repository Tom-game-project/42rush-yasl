BASE64_ALPHABET = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789+/"
)


BASE64_INDEX = {c: i for i, c in enumerate(BASE64_ALPHABET)}


def base64_decode(encoded: str) -> bytes:
    decoded = bytearray()

    # 4文字ずつ処理
    # base64でencodeされた文字列は必ず4倍長になる
    for i in range(0, len(encoded), 4):
        block = encoded[i:i+4]
        padding = block.count("=")

        # '=' を 0 に置換して処理
        block = block.rstrip("=") + "A" * padding

        twenty_four_bits = 0

        twenty_four_bits = (twenty_four_bits << 6) | BASE64_INDEX[block[0]]
        twenty_four_bits = (twenty_four_bits << 6) | BASE64_INDEX[block[1]]
        twenty_four_bits = (twenty_four_bits << 6) | BASE64_INDEX[block[2]]
        twenty_four_bits = (twenty_four_bits << 6) | BASE64_INDEX[block[3]]

        # 24bit → 3バイト
        decoded.append((twenty_four_bits >> 16) & 0xFF)
        decoded.append((twenty_four_bits >> 8) & 0xFF)
        decoded.append((twenty_four_bits >> 0) & 0xFF)

        # パディング分のバイトを削除
        if padding:
            decoded = decoded[:-padding]

    return bytes(decoded)

import base64

decode = base64.b64encode("hello world".encode("utf-8"))
print(decode)

print(base64_decode(decode.decode("utf-8")))

