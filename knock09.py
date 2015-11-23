#!/usr/bin/env python
#coding:utf-8

#09 Typoglycemia
#スペースで区切られた単語列に対して各単語の末尾と先頭の文字は残し、それ以外の文字の順序を
#ランダムに並び替えるプログラムを作成せよ。
#ただし、長さが4以下の単語は並び替えない。

import random

def main():
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    print(" ".join(typogly(sentence)))


def typogly(words):
    words_ret = []

    for word in words.split():
        word_list = list(word)

        if len(word) > 4: #文字列の長さ4以上のみ処理
            word_mid = word_list[1:-1]
            random.shuffle(word_mid)
            word_list[1:-1] = word_mid
            words_ret.append("".join(word_list))
        else:
            words_ret.append(word)

    return words_ret


if __name__ == "__main__":
    main()
