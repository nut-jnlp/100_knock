# -*- coding: utf-8 -*-
with open('input.txt') as input_file:
    with open('un11_output.txt','w') as output_file:
        for line in input_file:
            line = line.replace("\t", " ")
            output_file.write(line)
