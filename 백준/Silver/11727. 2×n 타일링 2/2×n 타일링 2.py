import sys
input = sys.stdin.readline

n = int(input())
# 1<= n <= 1000

dp = [0] * (n+1)
if n < 3:
    print(2 * n - 1)
else:
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-2]*3 + dp[i-3]*2
    print(dp[n] % 10007)