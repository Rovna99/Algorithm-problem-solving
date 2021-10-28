import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if not n:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
