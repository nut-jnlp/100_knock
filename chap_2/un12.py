# -*- coding: utf-8 -*-
input_file = open('input.txt', 'r')
output1_file = open('col1.txt', 'w')
output2_file = open('col2.txt', 'w')

lines = input_file.readlines()

output1_file.write(lines[0])
output1_file.close()
output2_file.write(lines[1])
output2_file.close()
