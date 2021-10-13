import sys

N = int(sys.stdin.readline())
atm = list(map(int, sys.stdin.readline().split()))

atm.sort()
result = [atm[0]]
for i in range(1, len(atm)):
    result.append(result[i-1]+atm[i])

print(sum(result))