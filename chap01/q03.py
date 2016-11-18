# coding: utf-8

sentence = """\
Now I need a drink, alcoholic of course, \
after the heavy lectures involving quantum mechanics.\
"""

words = sentence.replace(",", "").replace(".", "").split()
nums = [len(word) for word in words]

print(nums)
