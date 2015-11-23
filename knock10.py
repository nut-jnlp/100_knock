#!/usr/bin/env python
#coding:utf-8

#10 行数のカウント

def main():
    with open("hightemp.txt") as f:
        list = f.readlines()

    print(len(list))


if  __name__ == "__main__":
    main()

#UNIXコマンドと実行結果
#wc -l hightemp.txt
#24 hightemp.txt
#
#オプション
#-c:バイト数,-l:行数,-L:最も長い行のバイト数
#-w:単語数のみ
