#!/usr/bin/env python
#coding:utf-8

#11 タブをスペースへ置換

def main():
    with open("hightemp.txt") as f:
        list = f.readlines()

    print("".join(list).expandtabs(1))


if __name__ == "__main__":
    main()


#UNIXコマンドと実行結果
#sed "s/\t/ /g" hightemp.txt
#expand -t 1 hightemp.txt

