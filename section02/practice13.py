#!/usr/bin/python3
# coding: utf-8

def main():
    with open("col1.txt") as col1, open("col2.txt") as col2:
        for line1, line2 in zip(col1, col2):
            print("{}\t{}".format(line1.strip(), line2.strip()))

if __name__ == "__main__":
    main()

