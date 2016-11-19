# -*- coding: UTF-8 -*-
word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = word.split(" ")
nums = {1, 5, 6, 7, 8, 9, 15, 16, 19}
symbol = {}
for i in range(len(words)):
	if i+1 in nums:
		symbol[words[i][0]] = i+1
	else:
		symbol[words[i][:2]] = i+1

print(symbol)

