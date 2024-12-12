import sys
input = sys.stdin.readline

T = int(input().strip())

dp = [0] * 11
def f(num):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, num+1):
        if dp[i]:
            continue
        if i > 1:
            dp[i] += dp[i - 1]
        if i > 2:
            dp[i] += dp[i - 2]
        if i > 3:
            dp[i] += dp[i - 3]
    return dp[num]

for tc in range(T):
    n = int(input().strip())
    print(f(n))