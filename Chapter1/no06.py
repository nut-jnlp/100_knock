# -*- coding:utf-8 -*-

words1 = u"paraparaparadise"
words2 = u"paragraph"

def main():
	X = set(ngram(words1, 2))
	Y = set(ngram(words2, 2))
	print X | Y
	print X - Y
	print X & Y
	print "se" in X & Y

def ngram(sequence, n):
	for i in range(len(sequence) - n + 1):
		yield sequence[i:i + n]

	return

if __name__ == "__main__":
	main()
