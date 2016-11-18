# coding: utf-8

sentence = """\
Now I need a drink, alcoholic of course, \
after the heavy lectures involving quantum mechanics.\
"""

words = sentence.replace(",", "").replace(".", "").split()
nums = list(map(len, words))

print(nums)
