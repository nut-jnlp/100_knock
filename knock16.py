#!/usr/bin/env python3.4.3
#coding:utf-8

#16 ファイルをN分割する
import sys

def main():
    #コマンドライン引数の受け取り
    argvs = sys.argv
    argvs[2] = int(argvs[2])
    arglen = len(argvs)
    #引数が足りない場合の処理
    if arglen != 3:
        print("引数は3つ必要です")
        exit()

    with open(argvs[1]) as f:
        text = f.readlines()

        for i in range(argvs[2]-1):
            print("".join([text[i*argvs[2]+j] for j in range(int(len(text)/argvs[2]+1))]))
        print("".join(text[(i+1)*argvs[2]:]))

if __name__ == "__main__":
    main()

#UNIXコマンド
#split -l 5 hightemp.txt
