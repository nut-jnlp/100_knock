# coding:utf-8

import sys
from itertools import islice


def count_file_lines(f):
    for i, line in enumerate(f):
        pass
    f.seek(0)
    return i + 1


def devide_num(dividend, divisor):
    quotient = dividend // divisor
    remainer = dividend % divisor
    return (quotient + 1,) * remainer + (quotient,) * (divisor - remainer)


if __name__ == '__main__':
    args = sys.argv
    n = int(args[1])
    path = args[2]
    with open(path, "r") as f:
        total_line_num = count_file_lines(f)
        l = devide_num(total_line_num, n)
        for i, line_num in enumerate(l):
            with open("{}.{}".format(path, i), "w") as fout:
                for line in islice(f, line_num):
                    print(line, end="", file=fout)

# python q16.py 5 col1.txt
# split -l 5 col1.txt
