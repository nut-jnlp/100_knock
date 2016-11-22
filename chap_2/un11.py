# -*- coding: utf-8 -*-
a_file = open('input.txt', 'r')
b_file = open('output.txt', 'w')

for line in a_file:
    line = line.replace("\t", " ")
    print(line)
