# 問題1
i = 1
while i <= 5:
    print(i)
    i += 1

# 問題2
data = [1, 2, 3, 2, 4, 2, 5]
i = 0
while True:
    if data[i] == 2:
        del data[i]
    else:
        i += 1
    if 2 not in data:
        break
print(data)

# 問題3
n = 1
while True:
    if n > 1000:
        break
    n *= 2
print(n)

# 問題4
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)



