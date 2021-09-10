num = []


def sort(nums):
    if len(nums) <= 1:
        return

    half = len(nums) // 2
    left = nums[:half]
    right = nums[half:]
    sort(left)
    sort(right)

    i1, i2, ia = 0, 0, 0

    while i1 < len(left) and i2 < len(right):
        if left[i1] < right[i2]:
            nums[ia] = left[i1]
            i1 += 1
            ia += 1
        else:
            nums[ia] = right[i2]
            i2 += 1
            ia += 1
    while i1 < len(left):
        nums[ia] = left[i1]
        i1 += 1
        ia += 1
    while i2 < len(right):
        nums[ia] = right[i2]
        i2 += 1
        ia += 1


for i in range(int(input())):
    num.append(int(input()))

sort(num)
for i in num:
    print(i)
