# coding: utf-8
import fileinput

with open("col1.txt", "w") as col1_f, open("col2.txt", "w") as col2_f:
    for line in fileinput.input():
        col = line.split("\t")
        col1 = col[0]
        col2 = col[1]
        col1_f.write(col1 + "\n")
        col2_f.write(col2 + "\n")

# cut -f1 hightemp.txt > col1.txt && cut -f2 hightemp.txt > col2.txt
