#03 パトカー + タクシー　= パタトクカシー
#パトカーとタクシーの文字を先頭から交互に連結して文字列パタトクカシーを得よ

chara1 = "パトカー"
chara2 = "タクシー"
chara3 = ""

for i in range(0,4):
   chara3 += chara1[i] + chara2[i]

print(chara3)

