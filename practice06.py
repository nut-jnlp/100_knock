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
    _n_gram = []
    for i in range(len(seq) - (n - 1)):
        _n_gram.append((seq[i], seq[i + (n - 1)]))
    return _n_gram

if __name__ == "__main__":
    main()

