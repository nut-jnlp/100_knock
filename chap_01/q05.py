# -*- coding utf-8 -*-
# 05. n-gram

'''
N-gram : ある文字列の中でN個の文字列または単語の組み合わせがどの程度出現するかを調査する言語モデル
bi-gram : 2個の文字列の連鎖
単語bi-gram : 単語ごとの連鎖
文字bi-gram : 文字ごとの連鎖
'''

def n_gram(s):
	words = s.split(" ")
	comb1 = []
	for i in range(len(words)):
		if i == len(words) - 1:
			comb1.append(words[i])
		else:
			comb1.append(words[i] + " " + words[i+1])
	print("[単語bi-gram]")
	for i in range(len(words)):
		print(comb1[i])

	string = s.replace(" ", "")
	print(string)
	comb2 = []
	for i in range(len(string)):
		if i == len(string) - 1:
			comb2.append(string[i])
		else:
			comb2.append(string[i] + " " + string[i+1])
	print("[文字bi-gram]")
	for i in range(len(string)):
		print(comb2[i])

n_gram("I am an NLPer")
