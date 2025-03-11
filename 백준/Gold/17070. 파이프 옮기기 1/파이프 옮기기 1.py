import sys
input = sys.stdin.readline

n = int(input())
wall = list(list(map(int, input().split())) for _ in range(n))
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][1] = 1
# 세로 / 가로/ 대각선

for r in range(n):
    for c in range(n):
        if wall[r][c]: # 벽이면 넘어가
            continue
        if r > 0: #세로
            dp[r][c][0] += dp[r-1][c][0] + dp[r-1][c][2]

        if c > 0: #가로
            dp[r][c][1] += dp[r][c-1][1] + dp[r][c-1][2]

        if r > 0 and c > 0 and not wall[r-1][c] and not wall[r][c-1]:
            dp[r][c][2] += sum(dp[r-1][c-1])

print(sum(dp[n-1][n-1]))