#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentence_1 = "paraparaparadise"
sentence_2 = "paragraph"

def n_gram(elements,n):
    for element_index in xrange(0,len(elements)-n+1):
        yield elements[element_index:element_index+n]

# 集合：set リスト内表表記 重複は消される
X = set(n_gram(sentence_1,2))
Y = set(n_gram(sentence_2,2))

wa = X | Y
seki = X & Y
sa = X - Y

print "se" in X
print "se" in Y
print "se" in wa

print wa
print seki
print sa
