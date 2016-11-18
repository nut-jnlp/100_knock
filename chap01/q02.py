# coding: utf-8
from itertools import chain

word1 = "パトカー"
word2 = "タクシー"

merged_word = "".join(chain(*zip(word1, word2)))

print(merged_word)
