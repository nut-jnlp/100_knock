# -*- coding:utf-8 -*-

s1 = u"パトカー"
s2 = u"タクシー"

def main():
	print "".join([ c1 + c2 for c1, c2 in zip(s1, s2) ])

if __name__ == "__main__":
	main()
