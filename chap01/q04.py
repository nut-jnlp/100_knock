# coding: utf-8

sentence = """\
Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can."""
top_char = {1, 5, 6, 7, 8, 9, 15, 16, 19}

words = sentence.replace(",", "").replace(".", "").split(" ")
elms = dict(
    (w[:1], i+1) if i+1 in top_char else (w[:2], i+1)
    for i, w in enumerate(words)
)

print(elms)
