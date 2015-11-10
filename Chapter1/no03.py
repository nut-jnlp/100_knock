# -*- coding:utf-8 -*-

s = u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

def main():
	print map(len, s.replace(",", "").replace(".", "").split(" "))

if __name__ == "__main__":
	main()
