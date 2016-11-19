# -*- coding: utf-8 -*-
def n_gram_word(s, n):
    s = s.split(" ")
    if(n >= len(s)):
        return("Can't split")
    else:
        length = len(s)
        return [s[i:i+n] for i in range(0, length, n)]


def n_gram_str(s, n):
    if(n >= len(s)):
        return("Can't split")
    else:
        length = len(s)
        return [s[i:i+n] for i in range(0, length, n)]

s = "I am an NLPer"
n = 20

print(n_gram_word(s, n))
print(n_gram_str(s, n))
