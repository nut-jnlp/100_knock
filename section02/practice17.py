#!/usr/bin/python3
# coding: utf-8

def main():
    print(*set(map(lambda line: line.split()[0], open("hightemp.txt"))), sep="\n")

if __name__ == "__main__":
    main()

