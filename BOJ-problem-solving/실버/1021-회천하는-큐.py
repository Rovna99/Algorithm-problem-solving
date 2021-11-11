N, M = map(int, input())

num = list(map(int, input()))

for i in range(1, len(num)+1):
    while num:
        if i == num[0]:
            