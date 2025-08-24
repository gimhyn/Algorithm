import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
isCycle = False

for edge in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
cycle = set()

def dfs(prev, now, path):
    global isCycle
    if isCycle:
        return

    visited[now] = 1
    path.append(now)

    for vertex in graph[now]:
        if vertex == prev:
            continue
        if visited[vertex]:
            isCycle = True
            idx = path.index(vertex)
            cycle.update(path[idx:])
            return
        dfs(now, vertex, path)
        if isCycle:
            return
    path.pop()
    return

distance = [-1] * (n + 1)
def bfs():
    q = deque()
    for node in cycle:
        distance[node] = 0
        q.append(node)

    while q:
        now = q.popleft()

        for vertex in graph[now]:
            if distance[vertex] == -1:
                distance[vertex] = distance[now] + 1
                q.append(vertex)

    return

dfs(0, 1, [])
bfs()
print(*distance[1:])

