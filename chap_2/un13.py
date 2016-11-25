# -*- coding: utf-8 -*-
with open('col1.txt', 'r') as fin1, open('col2.txt', 'r') as fin2, \
     open('q13_merge.txt', 'w') as fout:
    for col1, col2 in zip(fin1, fin2):
        print(col1.replace('\n', '\t') + col2.replace('\n', ''), file=fout)
