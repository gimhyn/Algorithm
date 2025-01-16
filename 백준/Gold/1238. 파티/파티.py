import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, graph):
    distance = [float('inf')] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[0]
            if distance[node[1]] > cost:
                distance[node[1]] = cost
                heapq.heappush(q, (cost, node[1]))

    return distance

n, m, x = map(int, input().split())
g = [[] for _ in range(n+1)]
reverse_g = [[] for _ in range(n+1)] 

for _ in range(m):
    start, end, time = map(int, input().split())
    g[start].append((time, end))
    reverse_g[end].append((time, start))

togo = dijkstra(x, g)
tocome = dijkstra(x, reverse_g)

ans = 0
for i in range(1, n+1):
    if ans < togo[i] + tocome[i]:
        ans = togo[i] + tocome[i]

print(ans)