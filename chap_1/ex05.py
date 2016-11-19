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
