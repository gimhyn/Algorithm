import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [input().strip() for _ in range(r)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(row, col, bitmask, path):
    global max_path
    max_path = max(max_path, path)

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < r and 0 <= nc < c:
            idx = ord(board[nr][nc]) - 65
            if not (bitmask & (1 << idx)):  # 방문하지 않은 알파벳이라면
                dfs(nr, nc, bitmask | (1 << idx), path + 1)

max_path = 0
start_char = ord(board[0][0]) - 65
dfs(0, 0, 1 << start_char, 1)
print(max_path)
