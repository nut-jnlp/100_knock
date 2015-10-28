#!/usr/bin/env python
# -*- coding: utf-8 -*-

word_1 = u"パトカー"
word_2 = u"タクシー"

if len(word_1) >= len(word_2):
    loop = len(word_2)
else:
    loop = len(word_1)
output = ""
for n in xrange(0,loop):
    output = "".join([output, word_1[n], word_2[n]])

print output
