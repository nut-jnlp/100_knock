# -*- coding utf-8 -*-
# 07. テンプレートによる文生成

def template(x,y,z):
	print("%d時の%sは%.1f" % (x, y, z))

x = 12
y = "気温"
z = 22.4

template(x,y,z)


