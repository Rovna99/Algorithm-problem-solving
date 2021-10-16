
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a % b == 0 and a > b:
        print("multiple")
    elif b % a == 0 and b > a:
        print("factor")
    else:
        print("neither")

