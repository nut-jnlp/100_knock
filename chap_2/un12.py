# -*- coding: utf-8 -*-
with open('input.txt') as input_file:
    with open('col1.txt', 'w') as output1_file:
            with open('col2.txt', 'w') as output2_file:
                for line in iter(input_file.readlines()):
                    output1_file.writelines(line.split('\t')[0]+'\n')
                    output2_file.writelines(line.split('\t')[1]+'\n')
