# coding: utf-8

from __future__ import print_function, unicode_literals

def main():
    string = "パタトクカシーー"
    print("".join(c for i, c in enumerate(string) if i % 2 == 0))

if __name__ == "__main__":
    main()

