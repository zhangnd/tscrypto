from Crypto.Cipher import AES


def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


def main():
    key = b'5D18D1C81249C55E52A9669E9086E3DE'  # 密钥
    iv = b'0000000000000000'  # 初始化向量
    with open('', 'rb') as f:
        ciphertext = f.read()
        plaintext = decrypt(ciphertext, key, iv)
    with open('', 'wb') as f:
        f.write(plaintext)


if __name__ == '__main__':
    main()
