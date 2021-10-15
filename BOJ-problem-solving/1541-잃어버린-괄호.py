ep = input().split('-')
n = []
for i in ep:
    sum_n = 0
    s = i.split('+')
    for j in s:
        sum_n += int(j)
    n.append(sum_n)

result = n[0]
for i in range(1, len(n)):
    result -= n[i]

print(result)

