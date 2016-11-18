#! usr/bin/env python
# _*_ coding: utf-8 _*_

word1 = "パトカー"
word2 = "タクシー"
linking = ""

for (str1, str2) in zip(word1, word2):
    linking += (str1 + str2)
print(linking)
