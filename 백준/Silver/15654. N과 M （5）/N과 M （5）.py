import sys
input = sys.stdin.readline

def combi(arr, res, m):
    if len(res) == m:
        ans.append(tuple(res))
        return
    for i in range(len(arr)):
        if not used[i]:
            used[i] = 1
            combi(arr, res+[arr[i]], m)
            used[i] = 0

N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
# 수 10,000이하 N, M 8이하 자연수
ans = []
used = [0] * N
combi(nums, [], M)
ans.sort()

for lst in ans:
    print(*lst)