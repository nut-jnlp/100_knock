# -*- coding: utf-8 -*-
def n_gram_word(s, n):
    s = s.split(" ")
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]


def n_gram_str(s, n):
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

s = "I am an NLPer"
n = 2

print(n_gram_word(s, n))
print(n_gram_str(s, n))
