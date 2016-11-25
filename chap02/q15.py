# coding:utf-8

import sys
from collections import deque

args = sys.argv
n = int(args[1])
path = args[2]

with open(path, "r") as fin:
    print(*deque(fin, n), sep="", end="")
# python q15.py 4 col1.txt
# tail -n 4 col1.txt
