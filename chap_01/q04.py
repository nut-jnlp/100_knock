# cording -*- utf-8 -*-

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

#単語ごとに分割
words = s.split(" ")
#print(words)

n = [1,5,6,7,8,9,15,16,19]

dict = {}

for number,string in enumerate(words):
	if number+1 in n:
		dict[number+1] = string[:1:1]
	else:
		dict[number+1] = string[:2:1]

for key,value in dict.items():
	print("key: % d \t value: %s" % (key,value))

