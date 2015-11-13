# -*- coding:utf-8 -*-

import os

def main():
    hightemp = [row.strip().split("\t")[0] for row in open("hightemp.txt", "r")]
    hightemp = list(set(hightemp))
    hightemp.sort()
    for row in hightemp:
        print row

if __name__ == "__main__":
	main()

# 確認コマンド : cut -f 1 hightemp.txt | sort | uniq
