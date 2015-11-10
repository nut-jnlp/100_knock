#!/usr/bin/python3
# coding: utf-8

import sys
from collections import deque

def main():
    disp_num = int(sys.argv[1])
    for line in tail("hightemp.txt", disp_num):
        print(line, end='')

def tail(filename, n=None):
    return deque(open(filename), n)

if __name__ == "__main__":
    main()

