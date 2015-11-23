#!/usr/bin/env python3.4.3
#coding:utf-8

#04 元素記号
#"words" を単語ごとに分解し、文字数を先頭から順に並べたリストを作成する。
import re

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

list = ([w.strip(",.")for w in text.split()])

print (len(list))


