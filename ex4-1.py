# 問題１
number = 7
if number % 2 == 0:
    print('偶数')
else:
    print('奇数')

# 問題2
score = 85
if score >= 90:
    print('S')
elif score >= 80:
    print('A')
elif score >= 70:
    print('B')
else:
    print('C')

# 問題3
height = 130
age = 9
if height >= 120 and age >=10:
    print('乗車可能')
else:
    print('乗車不可')

# 問題4
x = 50
if 0 < x < 100:
    print('範囲内です')

# 問題5
is_member = True
purchase_amount = 5000
if is_member:
    if purchase_amount >= 3000:
        print("送料無料")
    else:
        print("送料500円")
else:
    print("送料1000円")
