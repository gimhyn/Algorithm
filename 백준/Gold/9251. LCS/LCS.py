import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

len1 = len(str1)
len2 = len(str2)
dp = [[0]*(len2 + 1) for _ in range(len1 + 1)]

for i in range(len1):
    for j in range(len2):
        if str2[j] == str1[i]:
            dp[i+1][j+1] += dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[len1][len2])