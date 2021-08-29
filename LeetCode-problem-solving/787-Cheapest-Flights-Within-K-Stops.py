import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])

        k = 0
        visited = {}
        Q = [(0, src, k)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            # 방문을 하지 않았다면 저장, 방문을 한 노드라면 더 적은 경유지로 왔을 경우에만 if문이 통과하도록 한다.
            if node not in visited or visited[node] > k:
                visited[node] = k
                for v, w in graph[node]:
                    if k <= K:
                        alt = price + w
                        heapq.heappush(Q, (alt, v, k + 1))
        return -1