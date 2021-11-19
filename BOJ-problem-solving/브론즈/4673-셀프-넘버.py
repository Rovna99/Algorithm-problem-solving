result = set(range(1, 10001))  # 범위 지정
del_num = set()  # 생성자가 있는 수들을 담을 set
for n in result:
    for i in str(n):  # 숫자의 한 자릿수씩
        n += int(i)  # n에다 더해준다.
    del_num.add(n)
result -= del_num  # 생성자가 있는 수들 제거
for i in sorted(result):
    print(i)
    