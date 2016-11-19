# -*- coding: utf-8 -*-
s = """Hi He Lied because Boron Could Not Oxidize Fluorine. New Nations Might
 Also Sign Peace Security Clause. Arthur King Can"""

s = s.replace(",", "").replace(".", "")
s = s.split(' ')
el = {}

indexs = [0, 4, 5, 6, 7, 8, 14 ,15 ,18]

for index, word in enumerate(s):
    if index in indexs:
        el[index+1] = word[0]
    else:
        el[index+1] = word[0]+word[1]

print(el)
