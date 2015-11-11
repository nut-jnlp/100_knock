# -*- coding:utf-8 -*-

import os

def main():
	hightemp = [row.strip().replace("\t", " ") for row in open("hightemp.txt", "r")]
	for row in hightemp:
		print row

if __name__ == "__main__":
	main()

# 確認コマンド : expand -t 1 hightemp.txt 
