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

if __name__ == "__main__":
    print(solve_10())
