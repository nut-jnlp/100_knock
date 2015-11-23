#!/usr/bin/env python3.4.3
#coding:utf-8

#13 col1.txtとcol2.txtをマージ

def main():
    with open("./section02/col1.txt") as col1,open("./section02/col2.txt") as col2:
        list1,list2 = col1.readlines(),col2.readlines()

    with open("./section02/col.txt","w") as col:
        for word1,word2 in zip(list1,list2):
            wlist = word1.strip("\n") +  " "+ word2.strip("\n") + "\n"
            print(wlist,end = "")
            col.write(wlist)

if __name__ == "__main__":
    main()

#UNIXコマンド
#paste col1.txt col2.txt -d" "
