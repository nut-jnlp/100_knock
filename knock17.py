#!/usr/bin/env python
#coding:utf-8

#17 1列目の文字列の異なり
import sys

def main():

    argvs = sys.argv

    with open(argvs[1]) as f:
        line = f.readlines()
        print("\n".join(set([w.split("\t")[0] for w in line])))


if __name__ == "__main__":
    main()

#UNIXコマンド
#cut -f1 hightemp.txt | sort | uniq

