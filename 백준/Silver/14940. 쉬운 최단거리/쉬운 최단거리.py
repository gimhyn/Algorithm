import sys
input = sys.stdin.readline 
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start = (i, j)
            break
            

visited = [[-1] * m for _ in range(n)]
sr, sc = start    
q = deque([(sr, sc)])    
visited[sr][sc] = 0
dx = [-1, 1, 0, 0]    
dy = [0, 0, -1, 1]
    
while q:
    r, c = q.popleft()
        
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
            
        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1 and board[nr][nc] == 1:
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            visited[i][j] = 0
       
for row in visited:
    print(*row)