import sys
from collections import deque

input = sys.stdin.readline

def bfs(sr, sc):
    if town[sr][sc] == '0':
        return 0

    cnt = 0
    q = deque()
    q.append((sr,sc))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        town[r][c] = '0'
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if town[nr][nc] == '1':
                    q.append((nr, nc))
                    town[nr][nc] = '0'

    return cnt


N = int(input())
# 5 <= N <= 25

town = list(list(input().strip()) for _ in range(N))
lst = []

for i in range(N):
    for j in range(N):
        num = bfs(i, j)
        if num:
            lst.append(num)

lst.sort()
print(len(lst))
for k in lst:
    print(k)
