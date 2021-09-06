weights = [50, 82, 75, 120]
head2head = ["NLWL", "WNLL", "LWNW", "WWLN"]


def solution(weights, head2head):
    rate = []
    heavy_w = [0]*len(weights)
    for i in range(len(weights)):
        wl = head2head[i].count("L") + head2head[i].count("W")
        if wl == 0:
            rate.append(0)
        else:
            rate.append(100*head2head[i].count("W")/wl)

        for j in range(len(weights)):
            if weights[i] < weights[j] and head2head[j][i] == "L":
                heavy_w[i] += 1

    result = []
    for i in range(len(weights)):
        result.append({'index': i+1, 'rate': rate[i], 'heavy_w': heavy_w[i], 'weights': weights[i]})

    result.sort(key=lambda x: x["weights"], reverse=True)
    result.sort(key=lambda x: x["heavy_w"], reverse=True)
    result.sort(key=lambda x: x["rate"], reverse=True)
    return [x['index'] for x in result]

# 감탄한 풀이
def solution(weights, head2head):
    result = []
    l = len(weights)
    # 한 번에 정렬해서 풀어봅시다!
    ans = [[0 for _ in range(4)] for _ in range(l)] # 승률, 무거운복서 이긴횟수, 자기 몸무게, 번호(음수로)
    for i in range(l):
        ans[i][2] = weights[i]
        ans[i][3] = -(i+1)
        cnt = 0 # 판수
        for j in range(l):
            if head2head[i][j] == 'W':
                ans[i][0] += 1 # 일단 이김
                cnt += 1
                if weights[i] < weights[j]:
                    ans[i][1] += 1 # 무거운 복서 이김
            elif head2head[i][j] == 'L':
                cnt += 1 # 판수만 늘려준다
        if cnt == 0:
            ans[i][0] = 0
        else:
            ans[i][0] /= cnt
    ans.sort(reverse=True) # 역순으로 정렬하면 모든 조건이 한 번에 정렬된다

    for i in range(l):
        result.append(-ans[i][3])
    return result



