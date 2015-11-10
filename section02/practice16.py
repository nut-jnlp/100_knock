#!/usr/bin/python3
# coding: utf-8

import sys
from itertools import zip_longest

def main():
    with open("hightemp.txt") as f:
        div_num = int(sys.argv[1])
        partial_file_lines = zip_longest(*[iter(f)]*div_num, fillvalue='')
        for i, lines in enumerate(partial_file_lines):
            output_file("output{}.txt".format(i), *lines, linefeed='')

def output_file(filename, *lines, linefeed='\n'):
    with open(filename, "w") as output:
        for line in lines:
            output.write(line + linefeed)

if __name__ == "__main__":
    main()

