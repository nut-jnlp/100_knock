# coding: utf-8
import fileinput

for line in fileinput.input():
    print(line.replace("\t", " "), end="")

# tr "\t" " " < hightemp.txt
