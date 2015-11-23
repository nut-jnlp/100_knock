#!/usr/bin/env python
#coding:utf-8

#08 暗号文
#以下の仕様で与えられた文字列を変換する関数cipherを実装せよ
#・英小文字ならば(219-文字コード)の文字に置換
#・その他の文字はそのまま出力

def cipher(words):

    return "".join([chr(219-ord(word))  if "a"<=word<="z" else word for word in
            words])


def main():
    words = "Hello World!"

    #暗号化
    print("暗号化 = ",cipher(words))
    #復号化
    print("復号化 = ",cipher(cipher(words)))


if __name__ == "__main__":
    main()
