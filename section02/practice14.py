#!/usr/bin/python3
# coding: utf-8

import sys

def main():
    with open("hightemp.txt") as f:
        disp_num = int(sys.argv[1])
        lines = f.readlines()
        print(*lines[:disp_num], sep='', end='')

if __name__ == "__main__":
    main()

