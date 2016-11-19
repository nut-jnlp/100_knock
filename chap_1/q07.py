#! usr/bin/env python
# _*_ cording utf-8 _*_

def create_sentence(x, y, z):
    print("{}時の{}は{}".format(x, y, z))

def main():
    create_sentence(12, "気温", 22.4)

if __name__ == '__main__':
    main()
