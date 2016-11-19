#! usr/bin/env python
# _*_ cording utf-8 _*_

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
periodic_table = {}
word_list = ""
number = [1, 5, 6, 7, 8, 9, 15, 16, 19]

word_list = sentence.replace(".", "").split()
for i, str in enumerate(word_list):
    if i+1 in number:
        periodic_table[i+1] = str[:1:1]
    else:
        periodic_table[i+1] = str[:2:1]
print(periodic_table)
