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

if __name__ == "__main__":
    # print(solve_10())
    print(solve_11())
