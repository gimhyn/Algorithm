import sys
input = sys.stdin.readline

N = int(input())
costs = []

for i in range(N):
    r, g, b = map(int, input().strip().split())
    costs. append([r, g, b])

dp = [[0] * 3 for _ in range(N)]

dp[0] = costs[0]
for j in range(1, N):
    for c in range(3):
        if dp[j-1][(c+1)%3] < dp[j-1][(c+2)%3]:
            dp[j][c] = dp[j-1][(c+1)%3] + costs[j][c]
        else:
            dp[j][c] = dp[j-1][(c+2)%3] + costs[j][c]

print(min(dp[N-1]))

