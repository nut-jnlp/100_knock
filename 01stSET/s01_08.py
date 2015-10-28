#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentence = "apple-!#23cat,:;DOG"

#文字列：string 文字:character
#文字コード化
def cipher(string):
    re_string = ""
    for char in string:
        re_string += char2cipher(char)
    return re_string


def char2cipher(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return chr(219-ord(char)) #ord()：アスキーコード取得,chr()：アスキーから文字
    else:
        return char


#python 内包表記　高速化
def cipher_new(string):
    return "".join([chr(219-ord(char)) if ord(char) >= 97 and ord(char) <= 122 else char for char in string])


def get_word2count(filename):
    return {word2count[line.strip().split()[0]] : int(line.strip().split()[1]) for line in open(filename) if 10000 >= int(line.strip().split()[1]) }


#print ord("a")#97
#print ord("z")#122
print cipher_new(sentence)
print cipher_new(cipher(sentence))
