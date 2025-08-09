import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    visited = [[0]*m for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if board[nr][nc] >= 1:
                    board[nr][nc] += 1
                    # 치즈는 접촉면 세야하니까 방문 처리 안하기
                else:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
    return

def melt():
    is_melted = 0
    bfs()
    for row in range(n):
        for col in range(m):
            if board[row][col] >= 3:
                board[row][col] = 0
                is_melted = 1
            elif board[row][col] == 2:
                board[row][col] = 1

    return is_melted

time = 0
while True:
    melted = melt()
    if not melted:
        print(time)
        break
    time += 1