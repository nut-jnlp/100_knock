#!/usr/bin/env python3.4.3
# -*- coding:utf-8 -*-

#n-gram
#wordsからn-gramを作る関数を作成せよ
#また、"I am an NLPer"という文から単語bi-gram,文字bi-gramを得よ

def main():
    text = "I am an NLPer"
    charas = list("".join(text.split()))
    words = text.split()

    print("_".join(ngram(charas,2))) #単語bi-gram
    print("_".join(ngram(words,2)))  #文字bi-gram


def ngram(text,n):

    return ["".join(text[i:i+n]) for i in range(len(text)-1)]


if __name__ == "__main__":
    main()

