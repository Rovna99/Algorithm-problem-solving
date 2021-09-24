import sys

input = sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -sys.maxsize
minimum = sys.maxsize
def cal(depth, total, plus, minus, multi, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        cal(depth + 1, total + n[depth], plus - 1, minus, multi, divide)
    if minus:
        cal(depth + 1, total - n[depth], plus, minus - 1, multi, divide)
    if multi:
        cal(depth + 1, total * n[depth], plus, minus, multi - 1, divide)
    if divide:
        cal(depth + 1, int(total / n[depth]), plus, minus, multi, divide - 1)


cal(1, n[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
