#! usr/bin/env python
# _*_ cording: utf-8 _*_

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quatum mechanics."
num_list = []

word_list = sentence.replace(",", "").replace(".", "").split()
print(word_list)

for i in range(len(word_list)):
    num_list += str(len(word_list[i]))
print(num_list)
