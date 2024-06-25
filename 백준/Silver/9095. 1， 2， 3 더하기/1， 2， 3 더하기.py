import sys
input = sys.stdin.readline

dp = [1] + [0] * 10
for j in range(1, 11):
    dp[j] += dp[j-1]
    if j > 1:
        dp[j] += dp[j-2]
    if j > 2:
        dp[j] += dp[j-3]

T = int(input())
for i in range(T):
    n = int(input())
    print(dp[n])