import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
if n == 1:
    print(1)
elif n == 2:
    print(2)    
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-2]+dp[i-1]
        # 2개 적은 거에 가로 넣기 + 1개 적은 거에 세로 넣기
        
    print(dp[n] % 10007)