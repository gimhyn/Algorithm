import sys
from heapq import heappop, heappush
input = sys.stdin.readline

V, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]

for edge in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def dijkstra(start):
    global V
    INF = 10e9
    distance = [INF] * (V+1)
    distance[start] = 0
    pq = []
    heappush(pq, (0, start))

    while pq:
        cost, now = heappop(pq)

        if distance[now] < cost:
            continue

        for val, next in graph[now]:
            if distance[next] > cost + val:
                distance[next] = cost + val
                heappush(pq, (cost+val, next))

    for i in range(1, V+1):
        print(distance[i] if distance[i] != INF else 'INF')
    return

dijkstra(k)