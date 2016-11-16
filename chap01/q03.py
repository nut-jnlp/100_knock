# coding: utf-8

sentence =\
    "Now I need a drink, alcoholic of course, "\
    "after the heavy lectures involving quantum mechanics."
words = sentence.replace(",", "").replace(".", "")
nums = []
for word in words.split():
    nums.append(len(word))
print(nums)
