#! /usr/bin/python3
# coding: utf-8

from functools import partial

def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"
    X = set(bi_gram(s1))
    Y = set(bi_gram(s2))
    print("X:", X)
    print("Y:", Y)
    print("X | Y:", X | Y)
    print("X & Y:", X & Y)
    print("X - Y:", X - Y)
    print('"se" in X and Y?', "se" in (X & Y))

def n_gram(seq, n):
    for item in zip(seq[:-(n - 1)], seq[n - 1:]):
        yield item
bi_gram = partial(n_gram, n=2)

if __name__ == "__main__":
    main()

