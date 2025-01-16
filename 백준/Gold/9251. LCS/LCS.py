import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

len1, len2 = len(str1), len(str2)

dl = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dl[i][j] = dl[i - 1][j - 1] + 1
        else:
            dl[i][j] = max(dl[i - 1][j], dl[i][j - 1])

print(dl[len1][len2])
