# coding: utf-8
import fileinput

with open("col1.txt", "w") as col1_f,\
        open("col2.txt", "w") as col2_f,\
        fileinput.input() as f_in:
    for line in f_in:
        col = line.split("\t")
        print(col[0], file=col1_f)
        print(col[1], file=col2_f)

# cut -f1 hightemp.txt > col1.txt && cut -f2 hightemp.txt > col2.txt
