# coding: utf-8

from __future__ import print_function, unicode_literals
from collections import OrderedDict

def main():
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = text.split(" ")
    elements = []
    for i, word in enumerate(words):
        i += 1
        if i == 1 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or \
                i == 15 or i == 16 or i == 19:
            elements.append(word[:1])
        else:
            elements.append(word[:2])
    d = OrderedDict()
    for element, word in zip(elements, words):
        d[element] = text.find(word)
    print(d.items())

if __name__ == "__main__":
    main()

