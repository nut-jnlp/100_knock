# coding: utf-8
import random

def rand1(word):
    if len(word) <= 4:
        return word
    m = list(word[1:-1])
    random.shuffle(m)
    return word[0] + "".join(m) + word[-1]



sentence = """\
I couldn't believe that I could actually understand \
what I was reading : the phenomenal power of the human mind .\
"""

print(" ".join(map(rand1, sentence.split())))
