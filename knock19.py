#!/usr/bin/env python
#coding:utf-8

#19 各行の1コラム目の文字列の出現頻度を求め、その高い順に並べて表示せよ。
#確認にはcut,uniq,sortコマンドを用いよ
import sys

def main():
    argvs = sys.argv

    with open(argvs[1]) as f:
        data = [w.split("\t")[0] for w in f.readlines()]
        lib = {word : data.count(word) for word in data}

        for num,name in sorted(lib.items(), key=lambda x:x[1], reverse = True):
            print(num,name)


if __name__ == "__main__":
    main()

#UNIXコマンド
#cut -f1 hightemp.txt | sort | uniq -c | sort -r
#uniq -c 入力された回数を出力
#sort -r 出力結果を逆順で出力
