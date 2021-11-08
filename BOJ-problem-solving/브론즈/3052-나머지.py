import sys

result = set()

for i in range(10):
    n = int(sys.stdin.readline())
    result.add(n % 42)

print(len(result))
