import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = sorted(set(list(map(int, input().strip().split()))))

ans = []

def perm(depth, index):
    if depth == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(index, len(nums)):
        ans.append(nums[i])
        perm(depth+1, i)
        ans.pop()

perm(0, 0)
