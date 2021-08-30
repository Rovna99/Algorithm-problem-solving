n1, n2 = map(int, input().split())

result = []
i = 2
while True:
    #두 수가 공약수 일 경우
    if n1 % i == 0 and n2 % i == 0:
        #공약수를 추가해주고 n1,n2를 나눈수로 변화
        result.append(i)
        n1 = int(n1 / i)
        n2 = int(n2 / i)
        continue
    i += 1
    #둘 중 하나라도 i보다 작아진다면, 공약수가 더 이상 없으므로 종료
    if n1 < i or n2 < i:
        break

max_factor = 1
min_multiple = 1

for i in range(len(result)):
    # 공약수를 하나씩 곱해줘서 최대 공약수를 구해준다.
    max_factor *= result[i]
# 최소공배수 = (최대공약수 * 각각의 서로소)이기때문에 쉽게 구해준다
min_multiple = n1 * n2 * max_factor
print(max_factor)
print(min_multiple)
