#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain


def solve_00():
    """
00. 文字列の逆順
    文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    """
    word = 'stressed'
    print(word[::-1])


def solve_01():
    """
    01. 「パタトクカシーー」
    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    """
    word = "パタトクカシーー"
    print(word[::2])


def solve_02():
    """
    02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
    「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    """
    word1 = 'パトカー'
    word2 = 'タクシー'
    chars = chain.from_iterable(zip(word1, word2))
    print(''.join(chars))

if __name__ == "__main__":
    solve_00()
    solve_01()
    solve_02()
