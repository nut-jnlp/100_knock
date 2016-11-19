# coding: utf-8
import fileinput

n = 0
for line in fileinput.input():
    n = n + 1
print(n)
# wc -l hightemp.txt
