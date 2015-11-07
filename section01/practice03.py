#! /usr/bin/python3
# coding: utf-8

def main():
    text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words = text.split(" ")
    print(*map(len, [word.strip(",.") for word in words]))

if __name__ == "__main__":
    main()

