# coding: utf-8
import random


def typoglycemia(sentence):
    words = sentence.split()
    return " ".join(map(random_sort_middle, words))


def random_sort_middle(word):
    if len(word) <= 4:
        return word
    top = word[0]
    bottom = word[-1]
    middle = list(word[1:-1])
    random.shuffle(middle)
    return top + "".join(middle) + bottom


sentence = """\
I couldn't believe that I could actually understand \
what I was reading : the phenomenal power of the human mind .\
"""
print(typoglycemia(sentence))
