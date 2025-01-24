import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * N
path = []

def perm(n, m):
    if len(path) == m:
        print(*path)
        return

    for i in range(n):
        if visited[i]:
            continue
        path.append(nums[i])
        visited[i] = 1
        perm(n, m)
        path.pop()
        visited[i] = 0

perm(N, M)
