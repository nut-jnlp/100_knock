#! /usr/bin/python3
# coding: utf-8

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

def bi_gram(seq):
    return n_gram(seq, 2)

def n_gram(seq, n):
    return (item for item in zip(seq[:-(n - 1)], seq[n - 1:]))

if __name__ == "__main__":
    main()

