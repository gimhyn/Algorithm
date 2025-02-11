import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [1]+[0]*m
    for coin in coins:
        for j in range(1, m+1):
            if j >= coin:
                dp[j] += dp[j-coin]

    print(dp[m])