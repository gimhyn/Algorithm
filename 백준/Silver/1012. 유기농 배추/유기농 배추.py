import sys
input = sys.stdin.readline

def dfs(tr, tc, arr):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    stack = []
    stack.append((tr, tc))
    while stack:
        r, c = stack.pop()
        arr[r][c] = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
                stack.append((nr, nc))
    return



T = int(input().strip())
for tc in range(T):
    M, N, K = map(int, input().split())
    # M, N 최대 50, K 최대 25
    bat = list([0] * M for _ in range(N))
    baechus = []
    for i in range(K):
        x, y = map(int, input().split())
        bat[y][x] = 1
        baechus.append((y, x))
    cnt = 0
    for baechu in baechus:
        r, c = baechu
        if bat[r][c]:
            cnt += 1
            dfs(r, c, bat)
    print(cnt)