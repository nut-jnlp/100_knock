# -*- coding:utf-8 -*-

import os

def main():
	hightemp = [row.strip().split("\t") for row in open("hightemp.txt", "r")]
	col1 = open("col1.txt", "w")
	col2 = open("col2.txt", "w")
	for row in hightemp:
		col1.write(row[0] + "\n")
		col2.write(row[1] + "\n")
	
	col1.close()
	col2.close()

if __name__ == "__main__":
	main()

# 確認コマンド : cut -f 1 hightemp.txt
#              : cut -f 2 hightemp.txt
