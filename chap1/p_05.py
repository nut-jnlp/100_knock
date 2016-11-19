# -*- coding: UTF-8 -*-
def Ngram(wd,n):
	ngram=[]
	if len(wd)>=n:
		for i in range(len(wd)-n+1):
			ngram.append(wd[i:i+n])
	return ngram

word = "I am an NLPer"
print(Ngram(word, 2))
print(Ngram(word.split(" "), 2))

