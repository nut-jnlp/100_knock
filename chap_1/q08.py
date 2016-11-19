#! usr/bin/env python
# _*_ cording utf-8 _*_

def cipher(sentence):
    # encryption / decryption
    result = ""
    for c in sentence:
        if c.islower() == True:
            result += chr(219 - ord(c))
        else:
            result += c
    return result

def main():
    sentence = "Hello World !"
    print("原文\t{}".format(sentence))
    # 暗号化
    encryption_text = cipher(sentence)
    print("暗号文\t{}".format(encryption_text))
    # 復号化
    decryption_text = cipher(encryption_text)
    print("復号文\t{}".format(decryption_text))

if __name__ == '__main__':
    main()
