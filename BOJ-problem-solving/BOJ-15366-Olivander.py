n = int(input())
# X는 지팡이의 크기를, Y는 상자 크기를 저장
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]
# sort를 해준다. -> 서로 순서정렬을 해서 하나라도 맞지 않는다면,
# 지팡이가 하나 남기 때문에 다 넣을 수 없다는 뜻이 된다.
X.sort()
Y.sort()
error = 0
# 만약 지팡이가 상자보다 크거나 작은게 1개라도 존재할 시, 에러를 올려 실패 표시
for i in range(n):
    if not X[i] <= Y[i]:
        error += 1
if error == 0:
    print("DA")
else:
    print("NE")
