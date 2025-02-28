import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    visited = [0] * (v+1)
    dist = [0] * (v+1)
    stack = deque([(0, start)])
    visited[start] = 1

    while stack:
        cost, now = stack.pop()

        for next, val in graph[now]:
            if not visited[next]:
                visited[next] = 1
                dist[next] = dist[now] + val
                stack.append((dist[next], next))

    return (dist.index(max(dist)), max(dist))

v = int(input())
graph = [[] for _ in range(v+1)]

for i in range(v):
    nums = list(map(int, input().replace("-1", "").split()))
    start = nums[0]
    for j in range(1, len(nums), 2):
        e, c = nums[j], nums[j+1]
        graph[start].append((e, c))

print(dfs(dfs(1)[0])[1])
