# -*- coding: UTF-8 -*-
import random

def typoglycemia(sentence):
    words = sentence.split()
    return " ".join(map(random_sort_inner, words))


def random_sort_inner(word):
    if len(word) <= 4:
        return word
    char_inner = list(word[1:-1])
    random.shuffle(char_inner)
    return word[0] + "".join(char_inner) + word[-1]


sentence = """\
I couldn't believe that I could actually understand \
what I was reading : the phenomenal power of the human mind .\
"""

print(typoglycemia(sentence))
