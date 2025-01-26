import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
path = []
used = [0] * N

def combi(now):
    if len(path) == M:
        print(*path)
        return
        
    for i in range(now, N):
        if used[i]:
           continue
        path.append(nums[i])
        used[i] = 1
        combi(i+1)
        used[i] = 0
        path.pop()

combi(0)