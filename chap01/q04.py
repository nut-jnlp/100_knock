# coding: utf-8

sentence = """\
Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can."""
top_char = {1, 5, 6, 7, 8, 9, 15, 16, 19}

words = sentence.replace(",", "").replace(".", "").split(" ")
elms = map(
    lambda i_w: i_w[1][:1] if i_w[0]+1 in top_char else i_w[1][:2],
    enumerate(words)
)
elms_dic = {elm: i+1 for i, elm in enumerate(elms)}

print(elms_dic)
