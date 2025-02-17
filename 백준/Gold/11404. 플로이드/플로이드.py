import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    INF = float('inf')
    costs = [INF] * (n + 1)
    pq = [(0, start)]
    costs[start] = 0

    while pq:
        c, now = heapq.heappop(pq)
        if costs[now] < c:
            continue
        for v, next in routes[now]:
            if costs[next] > c + v:
                costs[next] = c + v
                heapq.heappush(pq, (c+v, next))

    for idx in range(1, n+1):
        if costs[idx] == INF:
            print(0, end=" ")
        else: print(costs[idx], end=" ")

    return print()


n = int(input()) #100
m = int(input()) #100,000

routes = [[] for _ in range(n + 1)]

for r in range(m):
    a, b, c = map(int, input().split())
    routes[a].append((c, b))

for i in range(1, n+1):
    dijkstra(i)