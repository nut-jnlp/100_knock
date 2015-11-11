# -*- coding:utf-8 -*-

import os,sys,collections

def main():
    if len(sys.argv) <= 1:
        return

    split_file = None
    for i,row in enumerate(open("hightemp.txt", "r")):
        if i % int(sys.argv[1]) == 0:
            if split_file != None:
                split_file.close()

            split_file = open("hightemp_" + str(i / int(sys.argv[1])) + ".txt", "w")
        split_file.write(row.strip() + "\n")

    if split_file != None:
        split_file.close()

if __name__ == "__main__":
    main()

# 確認コマンド : tail -n N hightemp.txt 
