import sys

N = int(sys.stdin.readline())
s = []
res = []
count = 1
no = 0
for i in range(N):
    num = int(sys.stdin.readline())

    while count <= num:
        s.append(count)
        res.append('+')
        count += 1

    if s[-1] == num:
        s.pop()
        res.append('-')
    else:
        no = 1

if no == 1:
    print('NO')
else:
    for i in res:
        print(i)
