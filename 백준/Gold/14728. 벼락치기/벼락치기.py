import sys
input = sys.stdin.readline

# 단원 개수, 총 시간
n, t = map(int, input().split())

dp = [0] * (t+1)
for _ in range(n):
    k, s = map(int, input().split())
    # 공부 시간, 배점
    for i in range(t, k-1, -1):  # 뒤에서부터 진행
        dp[i] = max(dp[i], dp[i-k] + s)  # i-k에서 k시간을 더했을 때 배점을 더한 값으로 갱신

print(dp[t])
