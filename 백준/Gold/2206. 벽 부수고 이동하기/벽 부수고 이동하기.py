import sys
from collections import deque
input = sys.stdin.readline

def bfs(sr, sc):
    q = deque([(sr, sc, 0, 1)])
    visited = [[[0, 0] for _ in range(m)]for __ in range(n)]
    # visted[r][c][0] = 벽 안 부수고 옴
    # visited[r][c][1] = 랄프했다
    visited[sr][sc][0] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c, ralph, cnt = q.popleft()

        if r == n-1 and c == m-1:
            return cnt

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] and not ralph and not visited[nr][nc][1]:
                    visited[nr][nc][1] = 1
                    q.append((nr, nc, 1, cnt+1))
                elif not board[nr][nc] and not visited[nr][nc][ralph]:
                    visited[nr][nc][ralph] = 1
                    q.append((nr, nc, ralph, cnt+1))

    return -1

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
print(bfs(0, 0))