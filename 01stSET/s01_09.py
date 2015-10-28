#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

sentece = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(sentece):
    r_sentence = []
    words = sentece.split()
    for word in words:
        if len(word) >= 4:
            word_senter = list(word[1:-1])
            random.shuffle(word_senter)
            r_sentence.append(word[0]+"".join(word_senter)+word[-1])
        else:
            r_sentence.append(word)
    return " ".join(r_sentence)


print typoglycemia(sentece)
