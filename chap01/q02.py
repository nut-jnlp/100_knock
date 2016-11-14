# coding: utf-8

word1 = "パトカー"
word2 = "タクシー"

char_list = []
for t in zip(word1, word2):
    for c in t:
        char_list.append(c)
merged_word = "".join(char_list)

print(merged_word)
