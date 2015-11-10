#! /usr/bin/python3
# coding: utf-8

from collections import OrderedDict

def main():
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = text.split(" ")
    target_elements = (1, 5, 6, 7, 8, 9, 15, 16, 19)
    elements = []
    for i, word in enumerate(words):
        if i + 1 in target_elements:
            elements.append(word[:1])
        else:
            elements.append(word[:2])
    d = OrderedDict()
    for element, word in zip(elements, words):
        d[element] = text.find(word)
    print(d.items())

if __name__ == "__main__":
    main()

