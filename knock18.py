#!/usr/bin/env python
#coding:utf-8

#18 各行を3コラム目の数値の降順にソート
import sys

def main():
    argvs = sys.argv

    with open(argvs[1]) as f:
        data = f.readlines()
        linedata = [w.split("\n") for w in data]
        for line in sorted(linedata, key=lambda x:linedata[2]):
            print("".join(line))


if __name__ == "__main__":
    main()
