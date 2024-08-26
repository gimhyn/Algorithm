import sys
input = sys.stdin.readline

n = int(input())
wines = list(int(input()) for _ in range(n))

dp = [0] * n
dp[0] = wines[0]

for i in range(1, n):
    if i == 1:
        dp[i] = dp[i-1] + wines[i]
    elif i == 2:
        dp[i] = max(wines[i-2] + wines[i], dp[i-1], wines[i-1] + wines[i])
    else:
        dp[i] = max(dp[i-2] + wines[i], dp[i-1], dp[i-3] + wines[i-1]+ wines[i])


print(max(dp))
