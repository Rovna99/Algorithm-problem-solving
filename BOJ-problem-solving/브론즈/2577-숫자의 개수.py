import collections
import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = A * B * C  # 세 수의 곱

result = [0 for i in range(10)]  # 숫자의 갯수를 세기위한 list

for i in str(D):  # int타입은 사용할 수 없으므로 str타입으로 바꿔서 사용
    result[int(i)] += 1  # str타입으로 사용했으니,
    # i는 다시 int형으로 바꿔 인덱스의 위치를 찾고, 각 숫자의 개수를 1씩 올려준다.

for i in result:
    print(i)
