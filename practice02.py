# coding: utf-8

from __future__ import print_function, unicode_literals

def main():
    str1 = "パトカー"
    str2 = "タクシー"
    string = ""
    for c1, c2 in zip(str1, str2):
        string += (c1 + c2)
    print(string)

if __name__ == "__main__":
    main()

