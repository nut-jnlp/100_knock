#!/usr/bin/env python3.4.3
# -*- coding:utf-8 -*-

#21 カテゴリ名を宣言している行の抽出
import re
import json

category = re.compile("\[\[category:.+\]\]", re.IGNORECASE) #大文字小文字の区別をしない
categoryJp = re.compile("\[\[カテゴリ:.+\]\]")

with open("jawiki-England.txt") as f, open("jawiki-England-Category.txt","w") as w:
    for line in f:
        if re.search(category, line) or re.search(categoryJp, line) :
            w.write(line)

#memo
#re.complete()のカッコ内の特殊文字
#[] 文字の集合を指定する [amk]なら"a" "m" "k" のいずれかとマッチする
#　　 今回は[]を文字として扱いたいため\[とした
#.　(改行以外の)任意の文字列にマッチする
#+　直前の文字に作用し、1回以上繰り返したものにマッチさせる
#　 ab+ ならaのあとにbが1回以上続いたものにマッチする
