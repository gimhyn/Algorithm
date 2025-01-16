import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    visited = [float('inf')] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if visited[now] < cost:
            continue

        for node in graph[now]:
            sum_cost = cost + node[0]
            if visited[node[1]] > sum_cost:
                visited[node[1]] = sum_cost
                heapq.heappush(q, (sum_cost, node[1]))

    return visited


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

cost_start = dijkstra(1)
cost_v1 = dijkstra(v1)
cost_v2 = dijkstra(v2)

res1 = cost_start[v1] + cost_v1[v2] + cost_v2[N] # 1->v1->v2->N
res2 = cost_start[v2] + cost_v2[v1] + cost_v1[N] # 1->v2->v1->N

if res1 < float('inf') and res2 < float('inf'):
    print(min(res1, res2))
else:
    print(-1)
