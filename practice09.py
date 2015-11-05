#! /usr/bin/python3
# coding: utf-8

import random

def main():
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(" ".join([typoglycemia(s) for s in text.split()]))

def typoglycemia(s):
    if len(s) <= 4:
        return s
    return s[0] + shuffled_string(s[1:-1]) + s[-1]

def shuffled_string(s):
    l = list(s)
    random.shuffle(l)
    return "".join(l)

if __name__ == "__main__":
    main()

