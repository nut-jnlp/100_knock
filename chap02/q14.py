# coding:utf-8
import sys

args = sys.argv
n = int(args[1])
path = args[2]

with open(path, "r") as fin:
    for idx, line in enumerate(fin):
        if n <= idx:
            break
        print(line, end="")
# python q14.py 4 col1.txt
# head -n 4 col1.txt
