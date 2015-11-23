#!/use/bin/env python3.4.3
#coding: UTF-8

#06 集合
#sentence1,sentence2に含まれる文字bi-gramの集合をそれぞれXとYとして求め、XとYの和集合、積集合、差集合を求めよ。
#更に"se"というbi-gramがXおよびYに含まれるかどうかを調べよ。

def main():

    text1 = "paraparaparadise"
    text2 = "paragraph"

    #文字bi-gram
    X = set([text1[i:i+2] for i in range(len(text1)-1)])
    Y = set([text2[i:i+2] for i in range(len(text2)-1)])

    print("X = ",X)
    print("Y = ",Y)

    #和集合
    print("和集合 = ",X.union(Y))
    #積集合
    print("積集合 = ",X.intersection(Y))
    #差集合
    print("差集合 = ",X.difference(Y))

    #"se"という単語が含まれているかどうか
    if "se" in X:
        print("Xには'se'が含まれています")
    else:
        print("Xには'se'が含まれていません")
    if "se" in Y:
        print("Yには'se'が含まれています")
    else:
        print("Yには'se'が含まれていません")

if __name__ == "__main__":
    main()
