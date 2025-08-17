import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    INF = 10e9
    distance = [INF] * (n+1)
    distance[start] = 0
    pq = []
    heappush(pq, (0, start))

    while pq:
        dist, now = heappop(pq)

        if dist > distance[now]:
            continue

        for v, cost in graph[now]:
            new_dist = dist+ cost
            if distance[v] > new_dist:
                distance[v] = new_dist
                heappush(pq, (new_dist, v))

    return distance[n]

print(dijkstra(1))