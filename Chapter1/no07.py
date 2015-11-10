# -*- coding:utf-8 -*-

import sys

def main():
	print templete("12", "気温", "22.4")

def templete(x, y, z):
	return  "{0} 時の {1} は {2}".format(x, y, z)

if __name__ == "__main__":
	main()
