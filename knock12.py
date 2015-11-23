
#!/usr/bin/env python3.4.3
#coding:UTF-8

#12 1列目をcol1.txtに2列目をcol2.txtに保存

def main():

    with open("hightemp.txt") as f:
        sentence = f.readlines()
        line1 = [(words.split("\t"))[0] for words in sentence]
        line2 = [(words.split("\t"))[1] for words in sentence]

    with open("./section02/col1.txt","w") as col1:
         col1.write("\n".join(line1))
    with open("./section02/col2.txt","w") as col2:
         col2.write("\n".join(line2))

if __name__ == "__main__":
    main()

#UNIXコマンド
#1列目
#cut -f1 hightemp.txt
#2列目
#cut -f2 hightemp.txt
