# -*- coding utf-8 -*-

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 空白ごとに分割
words = s.split(" ")

# 単語末尾の,を削除
for i in range(len(words)):
	words[i] = words[i].strip(',').strip('.')

# 辞書dictを初期化
dict = {}

# dictに単語と文字長の要素を追加
# format関数を使用
for i in range(len(words)):
	dict['{w}'.format(w=words[i])] = len(words[i])

# dictの内容を表示
'''
for k, v in dict.items():
	print (k, v)
'''

# valueの値でソート
for k, v in sorted(dict.items(), key=lambda x:x[1], reverse=True):
	print (k)
