#! usr/bin/env python
# _*_ cording utf-8 _*_

import copy

sentence1 = "paraparaparadise"
sentence2 = "paragraph"

def get_bi_gram(sentence):
    result = []
    for i in range(len(sentence)):
        bi_gram = sentence[i:i+2]
        if bi_gram not in result:
            result.append(bi_gram)
    return result

def get_union(X, Y):
    result = Y
    for str_x in X:
        if str_x not in Y:
            result.append(str_x)
    return result


def get_intersection(X, Y):
    result = []
    for str_x in X:
        if str_x in Y:
            result.append(str_x)
    return result

def get_difference_set(text, intersection):
    result = text

    for word in intersection:
        if word in text:
            result.remove(word)
    return result

def main():
    X = get_bi_gram(sentence1)
    Y = get_bi_gram(sentence2)

    print("Xの集合\n{}\n".format(X))
    print("Yの集合\n{}\n".format(Y))

    union = get_union(copy.deepcopy(X), copy.deepcopy(Y))
    intersection = get_intersection(copy.deepcopy(X), copy.deepcopy(Y))
    difference_set_XY = get_difference_set(copy.deepcopy(X), copy.deepcopy(intersection))
    difference_set_YX = get_difference_set(copy.deepcopy(Y), copy.deepcopy(intersection))

    print("XとYの和集合\n{}\n".format(union))
    print("XとYの積集合\n{}\n".format(intersection))
    print("X-Yの差集合\n{}\n".format(difference_set_XY))
    print("Y-Xの差集合\n{}\n".format(difference_set_YX))

    print("以下の集合に\"se\"が含まれているか。")
    print("X:{}".format("se" in X))
    print("Y:{}".format("se" in Y))

if __name__ == "__main__":
    main()
