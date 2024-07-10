import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
   if dp[r][c] != -1:
       return dp[r][c]

   dp[r][c] = 1
   for i in range(4):
       nr = dr[i] + r
       nc = dc[i] + c
       if 0 <= nr < n and 0 <= nc < n and bamboos[nr][nc] > bamboos[r][c]:
           dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)

   return dp[r][c]




n = int(input().strip())
# 1 <= n <= 500
bamboos = list(list(map(int, input().split())) for _ in range(n))
# 1 <= bamboo <= 1,000,000
dp = list([-1] * n for i in range(n))

res = 1
for row in range(n):
    for col in range(n):
        res = max(res, dfs(row, col))

print(res)
