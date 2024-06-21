import sys
input = sys.stdin.readline

N = int(input())
# 1 <= N <= 1000 명
P = sorted(list(map(int, input().split())))

res = 0
for i in range(N):
    res += P[i]*(N - i)

print(res)