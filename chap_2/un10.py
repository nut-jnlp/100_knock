# -*- coding: utf-8 -*-
line_number = 0
with open('input.txt') as input_file:
    for line in input_file:
        line_number += 1

    print("行数:"+str(line_number))
