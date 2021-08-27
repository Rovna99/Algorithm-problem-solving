while True:
    num = list(map(int, input().split()))
    x = min(num)
    z = max(num)
    num.remove(x)
    num.remove(z)
    y = num[0]
    if x == 0 and y == 0 and z == 0:
        break
    if x ** 2 + y ** 2 == z ** 2:
        print('right')
    else:
        print('wrong')
