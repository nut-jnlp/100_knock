# -*- coding:utf-8 -*-

s = u"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

def main():
    one_char_list = [1, 5, 6, 7, 8 ,9 ,15, 16, 19]

    worddict = {}
    for i,word in enumerate(s.replace(",", "").replace(".", "").split(" ")):
        worddict[word[:1] if i + 1 in one_char_list else word[:2]] = i
    print worddict

if __name__ == "__main__":
	main()
