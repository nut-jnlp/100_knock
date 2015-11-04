#! /usr/bin/python3
# coding: utf-8

def main():
    string = "I am an NLPer"
    print(bi_gram(string.split()))
    print(bi_gram(string))

def bi_gram(seq):
    return n_gram(seq, 2)

def n_gram(seq, n):
    _n_gram = []
    for i in range(len(seq) - (n - 1)):
        _n_gram.append((seq[i], seq[i + (n - 1)]))
    return _n_gram

if __name__ == "__main__":
    main()

