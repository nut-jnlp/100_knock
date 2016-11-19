# -*- coding: UTF-8 -*-

word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
Words = ""
count = []
words = word.replace(",","").replace(".","").split(" ")
for i in range(len(words)):
	count.append(len(words[i]))
print(count)


