#!/usr/bin/env python3.4.3
#coding:utf-8

#14 先頭からN行を出力(head関数)
#15 末尾のN行を出力(tail関数)

def main():
    with open("./section02/col.txt") as f:
        list = f.readlines()

    print("".join(list))
    head(list,5)
    tail(list,5)


def head(input,n):
    """先頭からn行を出力"""
    print("".join([input[i] for i in range(n)]))

def tail(input,n):
    """末尾からn行を出力"""
    print("".join([input[i] for i in range(-n,0)]))


if __name__ == "__main__":
    main()

#UNIXコマンド
#先頭から5行
#head -n5 col.txt
#末尾から5行
#tail -n5 col.txt
