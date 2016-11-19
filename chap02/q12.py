# coding: utf-8
import fileinput

f_in = fileinput.input()
col1_f = open("col1.txt", "w")
col2_f = open("col2.txt", "w")
for line in f_in:
    col = line.split("\t")
    print(col[0], file=col1_f)
    print(col[1], file=col2_f)

# cut -f1 hightemp.txt > col1.txt && cut -f2 hightemp.txt > col2.txt
