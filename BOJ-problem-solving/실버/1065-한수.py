N = int(input())

cnt = 0
for i in range(1, N+1):
    m = list(map(int, str(i)))  # 자릿수를 한개씩 나눠 리스트에 저장
    if i < 100:  # 100전까진 모두 등차수열이다.
        cnt += 1
    elif m[0]-m[1] == m[1]-m[2]:  # 범위가 1000보다 작기때문에 1,2와 2,3만 비교
        cnt += 1
print(cnt)
