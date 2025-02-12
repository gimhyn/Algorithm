import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [-1] + [float('inf')]* n
    pq = [(0, start)] # 가중치, 노드 번호
    dist[start] = 0

    while pq:
        c, now = heapq.heappop(pq)
        if c > dist[now]:
            continue

        for v, next in tree[now]:
            cost = v + c
            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(pq, (cost, next))

    max_dist = max(dist)
    idx = dist.index(max_dist)
    return max_dist, idx

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    p, c, v = map(int, input().split())
    tree[p].append((v, c))
    tree[c].append((v, p))

temp, j = dijkstra(1)
ans, k = dijkstra(j)
print(ans)