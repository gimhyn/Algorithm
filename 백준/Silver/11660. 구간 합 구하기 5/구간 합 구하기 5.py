import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = list(list(map(int, input().split())) for _ in range(N))
dp = [[0] * (N+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, N+1):
        dp[r][c] = board[r-1][c-1] + dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1]

for turn in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
