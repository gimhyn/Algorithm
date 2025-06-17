import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]

def find_riped():
    q = deque()

    for r in range(m):
        for c in range(n):
            if box[r][c] == 1:
                q.append((r, c, 0))


    return q

def bfs():
    q = find_riped()

    total_day = 0
    while q:
        r, c, day = q.popleft()

        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < m and 0 <= nc < n and box[nr][nc] == 0:
                box[nr][nc] = day + 1
                q.append((nr, nc, day+1))
                total_day = day + 1

    for i in range(m):
        for j in range(n):
            if box[i][j] == 0:
                total_day = - 1
                break

    return total_day

print(bfs())

