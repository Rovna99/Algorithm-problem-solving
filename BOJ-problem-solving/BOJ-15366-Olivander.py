n = int(input())
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]
X.sort()
Y.sort()
error = 0
for i in range(n):
    if not X[i] <= Y[i]:
        error += 1
if error == 0:
    print("DA")
else:
    print("NE")
