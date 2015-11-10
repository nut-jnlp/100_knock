#!/usr/bin/python3
# coding: utf-8

import sys

def main():
    with open("hightemp.txt") as f:
        disp_num = int(sys.argv[1])
        for line in f:
            print(line, end='')
            disp_num -= 1
            if disp_num < 1:
                break

if __name__ == "__main__":
    main()

