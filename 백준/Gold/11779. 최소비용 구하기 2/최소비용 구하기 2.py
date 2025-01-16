import sys
import heapq

input = sys.stdin.readline

def djikstra(start, end):
    visited = [float('inf')] * (n+1)
    route = [[] for _ in range(n+1)]
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0
    route[start].append(start)

    while q:
        val, now = heapq.heappop(q)
        if visited[now] < val:
            continue

        for next in graph[now]:
            cost = val + next[0]
            if visited[next[1]] > cost:
                visited[next[1]] = cost
                route[next[1]] = route[now] + [next[1]]
                heapq.heappush(q, (cost, next[1]))

    return visited[end], len(route[end]), route[end]


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

s, e = map(int, input().split())

cost, cnt, route = djikstra(s, e)
print(cost)
print(cnt)
print(*route)
