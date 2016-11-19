#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain
import random


def solve_00():
    """
00. 文字列の逆順
    文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    """
    word = 'stressed'
    return word[::-1]


def solve_01():
    """
    01. 「パタトクカシーー」
    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    """
    word = "パタトクカシーー"
    return word[::2]


def solve_02():
    """
    02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
    「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    """
    word1 = 'パトカー'
    word2 = 'タクシー'
    chars = chain.from_iterable(zip(word1, word2))
    return ''.join(chars)


def solve_03():
    """
    03. 円周率
    "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    sentence = sentence.replace(',', '').replace('.', '')
    words = sentence.split(' ')

    charcter_nums = [len(word) for word in words]
    return charcter_nums


def solve_04():
    """
    04. 元素記号
    "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
    """
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    words = sentence.split(' ')

    target_nums = (1, 5, 6, 7, 8, 9, 15, 16, 19)
    picked = [(word[0], i) if i in target_nums else (word[:2], i)
              for i, word in enumerate(words, start=1)]

    return dict(picked)


def ngram(sequence, n=1):
    """
    シーケンスに対してngramを返す
    """
    assert(n > 0)
    return [sequence[i:i + n] for i in range(len(sequence) - n + 1)]


def solve_05():
    """
    05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    """
    sentence = 'I am an NLPer'
    return ngram(sentence, n=2), ngram(sentence.split(' '), n=2)


def solve_06():
    """
    06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    """
    word1 = 'paraparaparadise'
    word2 = 'paragraph'

    X = set(ngram(word1, n=2))
    Y = set(ngram(word2, n=2))

    return (X | Y), (X & Y), (X - Y), 'se' in (X & Y)


def solve_07(x, y, z):
    """
    07. テンプレートによる文生成
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
    """
    return "{x}時の{y}は{z}".format(x=x, y=y, z=z)


def solve_08(word):
    """
    08. 暗号文
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
    - 英小文字ならば(219 - 文字コード)の文字に置換
    - その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """
    def cipher(word):
        chars = [chr(219 - ord(char)) if char.islower()
                 else char for char in word]
        return ''.join(chars)

    return cipher(word)


def solve_09(sentence):
    """
    09. Typoglycemia
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
    """

    typoglycemia_words = []
    for word in sentence.split(' '):
        # 長さが4以下の単語は並び替えない
        if len(word) <= 4:
            typoglycemia_words.append(word)
            continue
        else:
            # 先頭と末尾
            char_head = word[0]
            char_tail = word[-1]

            # それ以外の文字の順序を並び替えた文字列を作成
            char_inner = list(word[1:-1])
            random.shuffle(char_inner)
            char_inner = ''.join(char_inner)

            typoglycemia_words.append(
                ''.join([char_head, char_inner, char_tail]))

    return ' '.join(typoglycemia_words)

if __name__ == "__main__":
    print(solve_00())
    print(solve_01())
    print(solve_02())
    print(solve_03())
    print(solve_04())
    print(solve_05())
    print(solve_06())
    print(solve_07(x=12, y="気温", z=22.4))

    english_message = "This is a message."
    cryped_message = solve_08(english_message)
    assert(solve_08(cryped_message), english_message)
    print(english_message, cryped_message, english_message, sep=' -> ')

    print(solve_09(sentence="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
