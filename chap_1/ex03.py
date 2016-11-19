# -*- coding: utf-8 -*-
s = """Now I need a drink, alcoholic of course, after the heavy lectures
 involving quantum mechanics."""
s = s.replace(",", "").replace(".", "")
s = s.split(' ')
print(s)

num = [len(s[a]) for a in range(15)]
print(num)