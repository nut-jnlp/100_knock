# coding:utf-8

import fileinput


if __name__ == '__main__':
    prefectures = {line.split("\t")[0] for line in fileinput.input()}
    print(*prefectures, sep="\n")

# python q17.py hightemp.txt
# cut -f1 hightemp.txt |sort|uniq
