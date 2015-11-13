# -*- coding:utf-8 -*-

import os,collections

def main():
    hightemp = [row.strip().split("\t")[0] for row in open("hightemp.txt", "r")]
    counter = collections.Counter(hightemp)
    for word, cnt in counter.most_common():
        print str(cnt) + " "  + word

if __name__ == "__main__":
	main()

# 確認コマンド : cut -f1 hightemp.txt | sort | uniq -c | sort -r 
