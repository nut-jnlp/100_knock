# -*- coding utf-8 -*-

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 空白ごとに分割
word = s.split(" ")

# 空白の回数
times = s.count(" ") #14

# 単語末尾の,を削除
for i in range(times):
	word[i] = word[i].strip(',')

# 辞書dictを初期化
dict = {}

# dictに単語と文字長の要素を追加
for i in range(times):
	dict['%s' % word[i]] = len(word[i])

# dictの内容を表示
'''
for k, v in dict.items():
	print (k, v)
'''

# valueの値でソート
for k, v in sorted(dict.items(), key=lambda x:x[1], reverse=True):
	print (k)
