# -*- coding: utf-8 -*-
def n_gram_str(s, n):
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]


s1 = "paraparaparadise"
s2 = "paragraph"

X = set(n_gram_str(s1, 2))
Y = set(n_gram_str(s2, 2))

print("X = "+str(X))
print("Y = "+str(Y))

print("intersection = "+str(X.intersection(Y)))
print("union = "+str(X.union(Y)))
print("difference = "+str(X.difference(Y)))

print("se" in list(X.union(Y)))
