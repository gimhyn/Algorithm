def findmin(num):
    dp = [0]*(num+1)
    if num == 1:
        return 0
    elif num < 4:
        return 1
    else:
        dp[2] = 1
        dp[3] = 1
        for i in range(4, num+1):
            dp[i] = dp[i-1] + 1
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i//3] + 1)
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i//2] + 1)

    return dp[num]


import sys
input = sys.stdin.readline

N = int(input())
print(findmin(N))
