#!/usr/bin/env python
# -*- coding: utf-8 -*-

text_file = "hightemp.txt"


def line_count(file_name):
    """
    行数のカウント
    :param file_name: 対象ファイル名
    :return:　int型で行数
    確認コマンド：wc hightemp.txt
    """
    text = open(file_name).readlines()
    #readlines()は大きいデータの時には非推薦(list型)
    return len(text)


def tab2space(file_name):
    """
    タブをスペースに置換
    :param file_name: 対象ファイル名
    :return: 文字列
    確認コマンド：sed -e "s/     / /g" hightemp.txt
    確認コマンド：diff hightemp_tab2space.txt hightemp_sed.txt ：確認
    """
    text = "".join(open(file_name).readlines())
    return text.replace("\t", " ")


def cut_column(file_name):
    """
    1列目をcol1.txtに，2列目をcol2.txtに保存
    :param file_name: 対象ファイル名
    確認コマンド：cut -f 1 hightemp.txt > hightemp_cut1.txt
    確認コマンド：cut -f 2 hightemp.txt > hightemp_cut2.txt
    確認コマンド：diff hightemp_cut1.txt col1.txt
    確認コマンド：diff hightemp_cut2.txt col2.txt
    """
    f1 = open("col1.txt", "w")
    f2 = open("col2.txt", "w")

    text = open(file_name)
    for line in text:
        words = line.split("\t")
        f1.write(words[0]+"\n")
        f2.write(words[1]+"\n")


def cut_column_2(file_name, column_num):
    """
    cut_column() を使いやすく改造。
    指定された列を返す。
    :param file_name: 対象ファイル名
    :param column_num: 指定の列番号
    :return: list型
    """
    text = open(file_name)
    column = []
    for line in text:
        words = line.split("\t")
        column.append(words[column_num-1])
    return column


def text_marge(file_name):
    """
    col1.txtとcol2.txtをマージ
    :param file_name: 対象ファイル名
    確認コマンド：paste col1.txt col2.txt > hightemp_paste.txt
    確認コマンド：diff hightemp_paste.txt hightemp_marge.txt
    """
    f1 = open("col1.txt")
    f2 = open("col2.txt")
    f3 = open("hightemp_marge.txt", "w")

    for word1 in f1:
        word2 = f2.readline()
        f3.write(word1.rstrip()+"\t"+word2)


def output_head(file_name, num):
    """
    先頭からN行を出力
    :param file_name:対象ファイル名
    :return: 文字列
    確認コマンド：head -3 hightemp.txt
    """
    texts = open(file_name)
    buf = ""
    for tmp in xrange(num):  # xrangeとrangeの違い
        # print tmp,texts.readline().rstrip() #readlineするとlist型になる
        # 型が異なる者同士のprintは , でOK
        buf += texts.readline()  # readlineするとlist型になる
    return buf


def output_tail(file_name, num):
    """
    末尾のN行を出力
    :param file_name: 対象ファイル名
    :return:　文字列
    確認コマンド：tail -3 hightemp.txt
    """
    texts = open(file_name)
    buf = ""
    Num_lines = line_count(file_name)
    for count in xrange(Num_lines):
        if count >= Num_lines-num:
            buf += texts.readline()
        else:
            texts.readline()
    return buf


def file_split(file_name, num):
    """
    行単位でファイルをN分割する
    :param file_name: 対象ファイル名
    確認コマンド：split -l 5 hightemp.txt output_higttemp.
    """
    texts = open(file_name)
    Num_lines = line_count(file_name)
    if Num_lines % num == 0:
        range_num = Num_lines/num
    else:
        range_num = 1+(Num_lines/num)
    for count in xrange(range_num):
        w_name = "split_"+str(count)+".txt"
        w_file = open(w_name, "w")
        for w_count in xrange(num):
            w_file.write(texts.readline())


def find_uniq(file_name):
    """
    １列目の文字列の異なり
    :param file_name: 対象ファイル名
    :return: set型
    確認コマンド：cat hightemp.txt | cut -f 1 |sort -k1 |uniq
    """
    column_1 = cut_column_2(file_name, 1)
    column_set = set()
    for word in sorted(column_1):
        column_set.add(word)
    return column_set


def val_sort(file_name, order):
    """
    各行を3コラム目の数値の降順にソート
    :param file_name: 対象ファイル名
    :param order: 0:昇順, 1：降順
    :return: 文字列
    確認コマンド：cat hightemp.txt | sort -k 3 -r
    """
    texts = open(file_name)
    buf = ""
    temp2line = {}  # 辞書型で保持
    text2line = {}
    del_set = set()
    num = 0
    for line in texts:
        ken, shi, temp, day = line.split("\t")
        text2line[num] = (ken, shi, temp, day)
        temp2line[num] = temp
        num += 1
    sort_temp = sorted(temp2line.items(), key=lambda x: x[1], reverse=order)
    for num_temp in xrange(len(sort_temp)):
        for num_text in xrange(len(text2line)):
            if sort_temp[num_temp][1] == text2line[num_text][2]:
                if num_text not in del_set:
                    buf = buf+"\t".join(text2line[num_text])
                    del_set.add(num_text)
    return buf


#print line_count(text_file)
#print tab2space(text_file)
#cut_column(text_file)
#text_marge(text_file)
#print output_head(text_file, 7)
#print output_tail(text_file, 7)
#file_split(text_file, 5)
#print "\n".join(find_uniq(text_file))
print val_sort(text_file, 1)
