result = set(range(1, 10001))
del_num = set()
for n in result:
    for i in str(n):
        n += int(i)
    del_num.add(n)
result -= del_num
for i in sorted(result):
    print(i)