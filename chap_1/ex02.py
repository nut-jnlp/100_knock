# -*- coding: utf-8 -*-
word1 = "パトカー"
word2 = "タクシー"

s = [s1+s2 for s1, s2 in zip(word1, word2)]
print("".join(s))
