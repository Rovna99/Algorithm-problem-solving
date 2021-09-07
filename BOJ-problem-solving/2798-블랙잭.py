# 브루트포스
N, M = map(int, input().split())
card = list(map(int, input().split()))
result = 0
for i in range(0, len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            if card[i]+card[j]+card[k] <= M:
                result = max(result, card[i]+card[j]+card[k])
print(result)

# 조합이용
from itertools import combinations

N, M = map(int, input().split())
card = list(map(int, input().split()))
cardCombination = list(combinations(card, 3))
max_Com = 0

for three_card in cardCombination:
    if max_Com < sum(three_card) <= M:
        max_Com = sum(three_card)

print(max_Com)
