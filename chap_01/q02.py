# -*- coding uft-8 -*-

word = ""
s1 = "パトカー"
s2 = "タクシー"

'''
for i in range(4):
	print(s1[i]+s2[i], end='')
print()
'''

# zip関数：複数のシーケンスをまとめてループ
for s1,s2 in zip(s1,s2):
	print(s1+s2,end="")
print("")