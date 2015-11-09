#03 パトカー + タクシー　= パタトクカシーー
#パトカーとタクシーの文字を先頭から交互に連結して文字列パタトクカシーーを得よ

words1 = "パトカー"
words2 = "タクシー"

print (("".join(["".join((word1,word2)) for (word1,word2) in zip(words1, words2)])))



#memo
#sep.join(seq) --> sepを区切り文字として,seqを連結する
#zip(list1,list2) --> list1とlist2を同時にループできる。要素数が異なる場合は少ない方に合わせる。
#内包処理 []で囲む
