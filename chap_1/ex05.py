# -*- coding: utf-8 -*-
def ngram_str(words, n):
    yield from zip(*(words[n:] for n in range(n)))


def ngram_word(words, n):
    words = words.split(" ")
    yield from zip(*(words[n:] for n in range(n)))


for num in ngram_str("I am a NLPer", 2):
    print(num)

print("\n")

for num in ngram_word("I am a NLPer", 2):
    print(num) 

#def n_gram_word(s, n):
#    s = s.split(" ")
#    if(n >= len(s)):
#       return("Can't split")
#   else:
#       length = len(s)
#        return [s[i:i+n] for i in range(0, length, n)]
#

#if n_gram_str(s, n):
#    if(n >= len(s)):
#        return("Can't split")
#    else:
#        length = len(s)
#        return [s[i:i+n] for i in range(0, length, n)]


#print(n_gram_str(s, n))

