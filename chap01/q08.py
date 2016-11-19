# coding: utf-8


def cipher(sentence):
    return "".join([chr(219-ord(c)) if c.islower() else c for c in sentence])


sentence = "Hello, Python!!"
print("原文 :" + sentence)
print("暗号化: " + cipher(sentence))
print("復号: " + cipher(cipher(sentence)))
