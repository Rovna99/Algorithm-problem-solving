# 병합 정렬..
num = []

def sort(num):
    if len(num) <= 1:
        return

    half = len(num) // 2
    left = num[:half]
    right = num[half:]
    sort(left)
    sort(right)

    i1, i2, ia = 0, 0, 0

    while i1 < len(left) and i2 < len(right):
        if left[i1] < right[i2]:
            num[ia] = left[i1]
            i1 += 1
            ia += 1
        else:
            num[ia] = right[i2]
            i2 += 1
            ia += 1
    while i1 < len(left):
        num[ia] = left[i1]
        i1 += 1
        ia += 1
    while i2 < len(right):
        num[ia] = right[i2]
        i2 += 1
        ia += 1


for i in range(int(input())):
    num.append(int(input()))


sort(num)

for i in num:
    print(i)

#2 파이썬 소트 사용용