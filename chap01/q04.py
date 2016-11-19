# coding: utf-8

sentence = """\
Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can."""
top_char = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = sentence.replace(",", "").replace(".", "").split(" ")
elms = map(
    lambda i, w: w[:1] if i+1 in top_char else w[:2],
    range(len(words)), words
)
elms_dic = dict(map(
    lambda i, w: (w, i+1),
    range(len(words)), elms
))

print(elms_dic)
