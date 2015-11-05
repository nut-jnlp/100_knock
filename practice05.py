#! /usr/bin/python3
# coding: utf-8

def main():
    string = "I am an NLPer"
    print(list(bi_gram(string.split())))
    print(list(bi_gram(string)))

def bi_gram(seq):
    return n_gram(seq, 2)

def n_gram(seq, n):
    return (item for item in zip(seq[:-(n - 1)], seq[n - 1:]))

if __name__ == "__main__":
    main()

