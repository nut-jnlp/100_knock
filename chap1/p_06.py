# -*- coding: UTF-8 -*-
def Ngram(wd,n):
    ngram=[]
        if len(wd)>=n:
            for i in range(len(wd)-n+1):
                ngram.append(wd[i:i+n])
        return ngram

word_1 = "paraparaparadise"
word_2 = "paragraph"

X = Ngram(word_1,1)
Y = Ngram(word_2,1)
print(set(X).union(Y))
print(set(X).difference(Y))
print(set(X).intersection(Y))
print(set(X).issuperset(Ngram("se",1)))
print(set(Y).issuperset(Ngram("se",1)))

