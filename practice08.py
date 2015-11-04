#! /usr/bin/python3
# coding: utf-8

def main():
    plain = "Hello, World!"
    print(cipher(plain))

def cipher(s):
    return "".join([c if not c.islower() else chr(219) for c in s])

if __name__ == "__main__":
    main()

