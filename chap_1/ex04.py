# -*- coding: utf-8 -*-
s = """Hi He Lied because Boron Could Not Oxidize Fluorine. New Nations Might
 Also Sign Peace Security Clause. Arthur King Can"""

s = s.replace(",", "").replace(".", "")
s = s.split(' ')
el = {}

for index, word in enumerate(s):
    if(word == s[0] or word == s[4] or word == s[5] or word == s[6]\
    or word == s[7] or word == s[8] or word == s[14] or word == s[15]\
    or word == s[18]):
        el[index+1] = word[0]
    else:
        el[index+1] = word[0]+word[1]

print(el)
