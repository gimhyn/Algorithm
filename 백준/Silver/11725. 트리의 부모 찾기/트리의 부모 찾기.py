import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, start):
    visited = [0] * (n+1)
    queue = deque([start])
    visited[start] = 1

    while queue:
        now = queue.popleft()
        for vertex in adj[now]:
            if not visited[vertex]:
                queue.append(vertex)
                visited[vertex] = 1
                par[vertex] = now


N = int(input())

adj = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().strip().split())
    adj[a].append(b)
    adj[b].append(a)

par = [[] for _ in range(N+1)]
bfs(N, 1)

for idx in range(2, N+1):
    print(par[idx])