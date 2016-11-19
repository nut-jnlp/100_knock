#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def solve_10():
    """
    10. 行数のカウント
    行数をカウントせよ．確認にはwcコマンドを用いよ．

    wc -l
    """
    line_num = 0
    for _ in sys.stdin:
        line_num += 1
    return line_num


def solve_11():
    """
    11. タブをスペースに置換
    タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

    cat hightemp.txt|tr $'\t' ' '
    """
    repl = lambda x: x.rstrip('\n').replace('\t', ' ')
    lines = (repl(line) for line in sys.stdin)

    return '\n'.join(lines)


def solve_12():
    """
    12. 1列目をcol1.txtに，2列目をcol2.txtに保存
    各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．


    """
    with open('./col1.txt', 'w') as fout_col1, open('./col2.txt', 'w') as fout_col2:
        for line in sys.stdin:
            cols = line.rstrip('\n').split('\t')

            fout_col1.writelines([cols[0], '\n'])
            fout_col2.writelines([cols[1], '\n'])


def solve_13():
    """
    13. col1.txtとcol2.txtをマージ
    12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

    paste col1.txt col2.txt
    """
    with open('./col1.txt', 'r') as fin_col1, open('./col2.txt', 'r') as fin_col2, \
            open('./merged_col.txt', 'w') as fout:
        for line1, line2 in zip(fin_col1, fin_col2):
            line1 = line1.rstrip()
            line2 = line2.rstrip()

            fout.writelines([line1, '\t', line2, '\n'])

if __name__ == "__main__":
    # print(solve_10())
    # print(solve_11())
    # solve_12()
    solve_13()
