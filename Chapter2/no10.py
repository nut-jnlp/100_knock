# -*- coding:utf-8 -*-

import os

def main():
	print len(open("hightemp.txt", "r").readlines())

if __name__ == "__main__":
	main()

# 確認コマンド : wc -l hightemp.txt
