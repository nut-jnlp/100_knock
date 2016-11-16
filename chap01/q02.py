# coding: utf-8

word1 = "パトカー"
word2 = "タクシー"

merged_word = "".join(["".join(t) for t in zip(word1, word2)])

print(merged_word)
