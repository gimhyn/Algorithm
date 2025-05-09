import sys
input = sys.stdin.readline


r, c = map(int, input().split())
board = list(input().strip() for _ in range(r))

def dfs(row, col, path):
    global max_path
    max_path = max(max_path, path)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < r and 0 <= nc < c and not visited[ord(board[nr][nc])-65]:
            visited[ord(board[nr][nc])-65] = 1
            dfs(nr, nc, path + 1)
            visited[ord(board[nr][nc])-65] = 0

    return max_path

max_path = 0
visited = [0] * 26
visited[ord(board[0][0])-65] = 1
print(dfs(0, 0, 1))
