import sys
input = sys.stdin.readline

def dfs(start):
    visited = [0] * (n+1)
    stack = [(0, start)]
    visited[start] = -1

    while stack:
        dist, now = stack.pop()

        for v, next in tree[now]:
            if not visited[next]:
                visited[next] = dist + v
                stack.append((dist + v, next))

    mv = max(visited)
    return mv, visited.index(mv)


n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    p, c, v = map(int, input().split())
    tree[p].append((v, c))
    tree[c].append((v, p))

temp, j = dfs(1)
ans, k = dfs(j)

print(ans)