import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().strip().split()))
dp = [0] * N

min_v = arr[0]
for i in range(1, N):
    min_v = min(min_v, arr[i-1])
    dp[i] = max(arr[i]-min_v, dp[i-1])

print(*dp)