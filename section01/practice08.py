#! /usr/bin/python3
# coding: utf-8

def main():
    plain_text = "I am an NLPer"
    print("plain text:", plain_text)
    cipher_text = cipher(plain_text)
    print("cipher text:", cipher_text)
    decrypted_text = decryption(cipher_text)
    print("decrypted text:", decrypted_text)

def cipher(s):
    return "".join([chr(219 - ord(c)) if c.islower() else c for c in s])

def decryption(s):
    return cipher(s)

if __name__ == "__main__":
    main()

