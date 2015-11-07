#!/usr/bin/python3
# coding: utf-8

def main():
    with open("hightemp.txt") as f, open("col1.txt", "w") as col1, open("col2.txt", "w") as col2:
        for line in f:
            columns = line.split(maxsplit=2)
            col1.write(columns[0] + "\n")
            col2.write(columns[1] + "\n")


if __name__ == "__main__":
    main()

