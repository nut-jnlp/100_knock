# -*- coding:utf-8 -*-

import os,sys

def main():
    if len(sys.argv) <= 1:
        return

    for i,row in zip(range(int(sys.argv[1])), open("hightemp.txt", "r")):
        print row.strip()

if __name__ == "__main__":
    main()

# 確認コマンド : head -n N hightemp.txt 
