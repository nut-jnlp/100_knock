#! usr/bin/env python
# _*_ coding: utf-8 _*_

word1 = "パトカー"
word2 = "タクシー"
linking = ""

lengh1 = len(word1)
lengh2 = len(word2)

for i in range(max(lengh1, lengh2)):
    linking += (word1[i] + word2[i])
print(linking)
