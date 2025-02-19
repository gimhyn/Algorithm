import sys
import heapq
input = sys.stdin.readline

def djikstra(start, graph):
    dist = [0] + [1e9]*n
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        c, now = heapq.heappop(pq)
        if dist[now] < c:
            continue

        for val, next in graph[now]:
            if dist[next] > val + c:
                dist[next] = val+c
                heapq.heappush(pq, (val+c, next))

    return dist

n, m, x = map(int, input().split())
togo = [[] for _ in range(n+1)]
tocome = [[] for _ in range(n+1)]

for i in range(m):
    s, e, t = map(int, input().split())
    togo[s].append((t, e))
    tocome[e].append((t, s))


res = [val1 + val2 for val1, val2 in zip(djikstra(x, togo), djikstra(x, tocome))]
print(max(res))