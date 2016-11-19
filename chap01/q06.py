# coding: utf-8


def ngram(n, word):
    return [tuple(word[i:i+n]) for i in range(len(word)-n+1)]


def print_var(var_name, var_param):
    print(var_name + ": \t", end="")
    print(var_param)


word1 = "paraparaparadise"
word2 = "paragraph"

x = set(ngram(2, word1))
y = set(ngram(2, word2))

print_var("X", x)
print_var("Y", y)
print_var("X|Y", set.union(x, y))
print_var("X&Y", set.intersection(x, y))
print_var("X-Y", x.difference(y))
print_var("Y-X", y.difference(x))
print_var("'se' in X", ('s', 'e') in x)
print_var("'se' in Y", ('s', 'e') in y)
