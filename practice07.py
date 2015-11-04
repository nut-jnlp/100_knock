#! /usr/bin/python3
# coding: utf-8

def main():
    print(template_string(x=12, y="気温", z=22.4))

def template_string(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

if __name__ == "__main__":
    main()

