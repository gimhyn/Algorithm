import sys
input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

board = [[0] * 101 for _ in range(101)]

def curve(x, y, d, g):
    directions = [d]

    for _ in range(g):
        for i in range(len(directions) - 1, -1, -1):
            directions.append((directions[i] + 1) % 4)

    board[y][x] = 1

    for dir in directions:
        x += dx[dir]
        y += dy[dir]
        if 0 <= x <= 100 and 0 <= y <= 100:
            board[y][x] = 1

for _ in range(n):
    x, y, d, g = map(int, input().split())
    curve(x, y, d, g)

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            cnt += 1

print(cnt)
