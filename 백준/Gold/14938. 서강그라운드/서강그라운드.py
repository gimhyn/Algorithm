import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m, r = map(int, input().split())
items = [0]+list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, now = heappop(pq)
        if dist[now] < cost:
            continue

        for next, val in graph[now]:
            if dist[next] > val + cost:
                dist[next] = val + cost
                heappush(pq, (val+cost, next))

    res = sum([items[x] for x in range(1, n+1) if dist[x] <= m])
    return res

ans = 0
for j in range(1, n+1):
    ans = max(ans, dijkstra(j))

print(ans)