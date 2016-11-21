# -*- coding: utf-8 -*-
line_number = 0
a_file = open('input.txt', 'r')
for line in a_file:
    line_number += 1

print(line_number)
