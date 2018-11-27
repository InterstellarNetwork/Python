#for文
#5から11未満まで=5~10
for i in range(5,11):
	print(i)

#listに関してもfor文で回せる
list = ["pizza", "chocolate", "ice cream"]
for food in list:
	print("I like eating " + food + ".")

#0から10になるまで1を足し続ける
x = 0
while x <= 10:
	print(x)
	x = x + 1

ages = {}
ages["Rob"] = 35
ages["Kirtsen"] = 36
ages["Tommy"] = 5
ages["Raphie"] = 1

for age in ages:
	print(age + " is " + str(ages[age]) + ".")
