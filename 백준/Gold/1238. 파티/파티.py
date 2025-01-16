import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, target=None):
    distance = [float('inf')] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            v, e = node
            cost = dist + v
            if distance[e] > cost:
                distance[e] = cost
                heapq.heappush(q, (cost, e))

    if target:
        return distance[target]
    else:
        return distance

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((time, end))

cost = dijkstra(x)
for i in range(1, n+1):
    cost[i] += dijkstra(i, x)

print(max(cost[1:]))