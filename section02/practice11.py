#!/usr/bin/python3
# coding: utf-8

def main():
    print(*map(lambda line: line.replace('\t', ' '), open("hightemp.txt")), sep="", end="")

if __name__ == "__main__":
    main()

