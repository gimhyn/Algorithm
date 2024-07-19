import sys

input = sys.stdin.readline

# H >= 0
# 1 <= N나무수 <= 1,000,000
# 1 <= M타겟 <= 2,000,000,000

N, M = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))


start = 0
end = max(trees)

while start <= end:
    res = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            res += tree - mid
    if res < M:
        end = mid - 1
    elif res > M:
        start = mid + 1
    else:
        break

print((start + end) // 2)
