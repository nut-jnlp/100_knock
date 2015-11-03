# coding: utf-8

from __future__ import print_function, unicode_literals

def main():
    plain = "Hello, World!"
    print(cipher(plain))

def cipher(s):
    return "".join([c if not c.islower() else unichr(219) for c in s])

if __name__ == "__main__":
    main()

