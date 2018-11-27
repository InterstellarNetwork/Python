#ver3以降はprintは()でくくる
#型推論＝データ型を自動で割り当てる。そのかわり型変換が必要
age = 35
print(age)

pi = 3.14
print(pi)

#stringは””でくくる
name = "Rob"
print(name)

print(age/pi)

#string
number = "5"
print(number * age)

#型変換
print(int(number) * 5)
print(int(number) * age)
print(int(number) * pi)


str = "My name is Rob"
#0番目
print(str[0])
#0番目から5番目まで=6文字分
print(str[0:5])
print(str[5])

#配列
myList = ["Apple", "banana", "orange"]
print(myList)
#0番飛ばして1番だけ
print(myList[1])
#1番から4番
print(myList[1:4])

#タプル型
#読み取り専用
myTuple = (1,2,3,4)
print(myTuple)
#変更しようとしても変わらない
#myTuple[1] = 5
#print(myTuple)

#ディクショナリ型
dict = {}
dict["dad"] = "Rob"
dict["mum"] = "Kirsten"
dict[1] = "Tommy"
dict[2] = "Raphie"

print(dict)
print(dict["mum"])
#キーだけを取り出すメソッド
print(dict.keys())
#値だけを取り出すメソッド
print(dict.values()
)
