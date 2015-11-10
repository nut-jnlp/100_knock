#!/usr/bin/python3
# coding: utf-8

from collections import Counter

def main():
    print(*map(lambda x: "{0[1]:-7} {0[0]}".format(x), Counter(map(lambda line: line.split()[0], open("hightemp.txt"))).most_common()), sep="\n")

if __name__ == "__main__":
    main()

