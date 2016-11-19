# coding -*- utf-8 -*-
# 06.集合

def bi_gram(s):
	comb = []
	for i in range(len(s)):
		if i == len(s) - 1:
			comb.append(s[i])
		else:
			comb.append(s[i] + s[i+1])
	'''
	print("[%s]" % a)
	for i in range(len(s)):
		print(comb[i])
	'''
	return comb

X_list = bi_gram("paraparaparadise")
Y_list =bi_gram("paragraph")

X_set = set(X_list)
Y_set = set(Y_list)

print("X: ", X_set)
print("Y: ", Y_set)

print("和集合：", X_set | Y_set)
print("積集合：", X_set & Y_set)
print("差集合：", X_set - Y_set)

