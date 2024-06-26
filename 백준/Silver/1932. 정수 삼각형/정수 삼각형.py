import sys
input = sys.stdin.readline

n = int(input())
tri = list(list(map(int, input().split())) for _ in range(n))

dp = list([0] * (i+1) for i in range(n))
dp[0] = tri[0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = tri[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = tri[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tri[i][j]


print(max(dp[n-1]))