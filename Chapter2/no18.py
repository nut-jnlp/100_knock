# -*- coding:utf-8 -*-

import os,collections

def main():
    hightemp = [row.strip().split("\t") for row in open("hightemp.txt", "r")]
    hightemp = sorted(hightemp, key=lambda row: row[2], reverse=True)
    for row in hightemp:
        print "\t".join(row)

if __name__ == "__main__":
	main()

# 確認コマンド : sort -k3 -r hightemp.txt 
