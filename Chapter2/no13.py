# -*- coding:utf-8 -*-

import os

def main():
    col1 = open("col1.txt", "r")
    col2 = open("col2.txt", "r")
    col12 = open("col12.txt", "w")
    for row1,row2 in zip(col1,col2):
        col12.write(row1.strip() + "\t" + row2.strip() + "\n")
    
    col1.close()
    col2.close()
    col12.close()

if __name__ == "__main__":
    main()

# 確認コマンド : paste col1.txt col2.txt 
