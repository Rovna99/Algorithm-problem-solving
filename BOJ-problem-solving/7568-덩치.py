w, h = [], []
rank = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    w.append(x)
    h.append(y)
    rank.append(1)
for i in range(len(w)):
    for j in range(len(w)):
        if w[i] < w[j] and h[i] < h[j]:
            rank[i] += 1

for i in rank:
    print(i, end=" ")
