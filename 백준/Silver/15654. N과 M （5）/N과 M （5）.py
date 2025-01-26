import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
path = []
used = [0] * N

def permutation():
    if len(path) == M:
        print(*path)
        return
        
    for i in range(N):
        if used[i]:
           continue
        path.append(nums[i])
        used[i] = 1
        permutation()
        used[i] = 0
        path.pop()

permutation()