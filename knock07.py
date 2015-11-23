#07 テンプレートによる文生成
#引数x,y,zを受け取り"x時のyはz"という文字列を返す関数を実装せよ
#また、x=12,y="気温",z=22.4として実行結果を確認せよ

def message(x,y,z):

    return print("{0}時の{1}は{2}".format(x,y,z))


def main():

    message(12,"気温",22.4)

if __name__ == "__main__":
    main()

