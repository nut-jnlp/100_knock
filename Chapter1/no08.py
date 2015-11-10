# -*- coding:utf-8 -*-

s = u"The quick brown fox jumps over the lazy dog."

def main():
	print chiper(s)

def chiper(s):
	return "".join([chr(219 - ord(c)) if c.islower() else c for c in s])

if __name__ == "__main__":
	main()
