import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

asc_dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            asc_dp[i] = max(asc_dp[i], asc_dp[j]+1)

desc_dp = [1] * n
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if A[i] > A[j]:
            desc_dp[i] = max(desc_dp[i], desc_dp[j]+1)

res = 1
for i in range(n):
    temp = asc_dp[i] + desc_dp[i] - 1
    res = max(temp, res)

print(res)