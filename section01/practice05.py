#! /usr/bin/python3
# coding: utf-8

from functools import partial

def main():
    string = "I am an NLPer"
    print(list(bi_gram(string.split())))
    print(list(bi_gram(string)))

def n_gram(seq, n):
    for item in zip(seq[:-(n - 1)], seq[n - 1:]):
        yield item
bi_gram = partial(n_gram, n=2)

if __name__ == "__main__":
    main()

