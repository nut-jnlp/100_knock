#!/usr/bin/python3
# coding: utf-8

def main():
    filename = "hightemp.txt"
    print(sum(1 for line in open(filename)), filename)

if __name__ == "__main__":
    main()

