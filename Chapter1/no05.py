# -*- coding:utf-8 -*-

s = u"I am an NLPer"

def main():
	for bigram in ngram(s, 2):
		print bigram
	for bigram in ngram(s.split(" "), 2):
		print bigram

def ngram(sequence, n):
	for i in range(len(sequence) - n + 1):
		yield sequence[i:i + n]

	return

if __name__ == "__main__":
	main()
