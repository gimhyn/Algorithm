import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    if n <= 3:
        print(1)
    else:
        dp = [0, 1, 1, 1] + [0] * (n-3)
        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2]
        print(dp[n])