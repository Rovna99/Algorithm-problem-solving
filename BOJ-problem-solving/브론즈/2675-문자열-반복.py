T = int(input())
for i in range(T):
    result = []
    a, b = input().split()
    for s in b:
        result.append(int(a)*s)

    print(''.join(result))