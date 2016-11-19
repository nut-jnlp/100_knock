# !/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import nlp100


def test_00():
    assert 'desserts' == nlp100.solve_00('stressed')


def test_01():
    assert nlp100.solve_01('パトカー', 'タクシー') == 'パタトクカシーー'


def test_02():
    assert 'パトカー' == nlp100.solve_02('パタトクカシーー')


def test_03():
    from itertools import zip_longest
    text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    right = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    ans = nlp100.solve_03(text)
    for r, a in zip_longest(right, ans):
        assert r == a


def test_04():
    import nlp100
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    ans = nlp100.solve_04(text)
    right = {
        'H': 1,
        'He': 2,
        'Li': 3,
        'Be': 4,
        'B': 5,
        'C': 6,
        'N': 7,
        'O': 8,
        'F': 9,
        'Ne': 10,
        'Na': 11,
        'Mi': 12,
        'Al': 13,
        'Si': 14,
        'P': 15,
        'S': 16,
        'Cl': 17,
        'Ar': 18,
        'K': 19,
        'Ca': 20,
    }
    assert all(ans[sym] == right[sym] for sym in right)


def test_05():
    words = "I am an NLPer".split()

    assert sum(1 for _ in nlp100.solve_05(words, 1)) == 4
    assert sum(1 for _ in nlp100.solve_05(words, 2)) == 3

    unigram = set(nlp100.solve_05(words, 1))
    print(unigram)
    assert all((w,) in unigram for w in words)
    for w in words:
        assert (w,) in unigram

    bigram = set(nlp100.solve_05(' '.join(words), 2))
    ans = [
        ('I', ' '), (' ', 'a'), ('a', 'm'), ('m', ' '), (' ', 'a'), ('a', 'n'),
        ('n', ' '), (' ', 'N'), ('N', 'L'), ('L', 'P'), ('P', 'e'), ('e', 'r')
    ]
    for w in ans:
        assert w in bigram


def test_06():
    # 和集合, 積集合 および 差集合 は今回重複無しで考える
    word1 = "paraparaparadise"
    word2 = "paragraph"
    right = [
        {
            ('d', 'i'), ('s', 'e'), ('r', 'a'), ('a', 'g'), ('a', 'r'),
            ('p', 'h'), ('p', 'a'), ('i', 's'), ('a', 'd'), ('a', 'p'),
            ('g', 'r')
        },
        {('r', 'a'), ('a', 'r'), ('a', 'p'), ('p', 'a')},
        {('i', 's'), ('a', 'd'), ('d', 'i'), ('s', 'e')}
    ]

    for r, a in zip(right, nlp100.solve_06(word1, word2)):
        for elm in r:
            assert elm in a

    # TODO:重複有りバージョン (返す値はdict), 和集合の定義確認


def test_07():
    assert "12時の気温は22.4" == nlp100.solve_07(12, '気温', 22.4)


def test_08():
    """
    08. 暗号文
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(nlp100.solve_09(text))



def test_09():
    """
    09. Typoglycemia
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以
    外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の
    単語は並び替えないこととする．適当な英語の文
    （例えば "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
    を与え，その実行結果を確認せよ．
    """
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    for word1, word2 in zip(text.split(), nlp100.solve_09(text).split()):
        assert word1[0] == word2[0]
        assert word1[-1] == word2[-1]
        assert len(word1) == len(word2)




if __name__ == '__main__':
    unittest.main()
