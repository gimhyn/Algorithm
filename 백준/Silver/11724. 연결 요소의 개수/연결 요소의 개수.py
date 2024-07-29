import sys
input = sys.stdin.readline
from collections import deque
def dfs(start):
    stack = [start]
    visited[start] = 1
    
    while stack:
        vertex = stack.pop()
        for node in connections[vertex]:
            if not visited[node]:
                visited[node] = 1
                stack.append(node)

N, M = map(int, input().split())
connections = list([]*(N + 1) for _ in range(N+1))
for i in range(M):
    u, v = map(int, input().split())
    connections[u].append(v)
    connections[v].append(u)

visited = [0] * (N + 1)
cnt = 0
for j in range(1, N+1):
    before = sum(visited)
    if not visited[j]:
        dfs(j)
        after = sum(visited)
        if before != after:
            cnt += 1
        

print(cnt)