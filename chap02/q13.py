# coding: utf-8

with open("col1.txt", "r") as col1_f,\
        open("col2.txt", "r") as col2_f,\
        open("col12.txt", "w") as col12_f:
    for col1, col2 in zip(col1_f, col2_f):
        print("{}\t{}".format(col1.rstrip("\r\n"),
                              col2.rstrip("\r\n")), file=col12_f)
# paste col1.txt col2.txt
