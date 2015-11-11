# -*- coding:utf-8 -*-

import os,sys,collections

def main():
    if len(sys.argv) <= 1:
        return

#    メモリ消費大
#    for row in open("hightemp.txt", "r").readlines()[-int(sys.argv[1]):]:

    for row in collections.deque(open("hightemp.txt", "r"), int(sys.argv[1])):
        print row.strip()

if __name__ == "__main__":
    main()

# 確認コマンド : tail -n N hightemp.txt 
