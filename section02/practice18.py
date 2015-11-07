#!/usr/bin/python3
# coding: utf-8

def main():
    print(*sorted(open("hightemp.txt"), key=lambda line: float(line.split()[2]), reverse=True), sep='')

if __name__ == "__main__":
    main()

