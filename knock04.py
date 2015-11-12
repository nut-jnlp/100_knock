#04 元素記号
#"words" を単語ごとに分解し、文字数を先頭から順に並べたリストを作成する。
import re

words = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = []

for word in re.split("\s|,\s|\.",words):
	list.append(len(word))
list.pop()
print(list)

#memo
#list.append("xxx") xxxをlistの最後に追加する
#re.split("xxx|yyy",word) wordをxxxとyyyで分割する(import re)
