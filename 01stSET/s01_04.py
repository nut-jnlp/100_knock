#!/usr/bin/env python
# -*- coding: utf-8 -*-

location = {1, 5, 6, 7, 8, 9, 15, 16, 19}
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split()

atom_list = {}
for num, word in enumerate(words, start = 1):
    if num in location:
        buf = word[0]
    else:
        buf = word[:2] 
    atom_list[buf] = num

print sorted(atom_list.items(), key=lambda x:x[1]) 



