import sys
input = sys.stdin.readline

def findmax(scores, n):
    dp = [0]*n
    if n == 1:
        return scores[0] 
    elif n == 2:
        return scores[0] + scores[1]        
        
    dp[0] = scores[0]
    dp[1] = scores[1] + scores[0]
    dp[2] = max(scores[0] + scores[2], scores[1]+ scores[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-3] + scores[i-1] + scores[i], dp[i-2]+scores[i])
    return dp[-1]

N = int(input())
scores = list(int(input()) for _ in range(N))

print(findmax(scores, N))