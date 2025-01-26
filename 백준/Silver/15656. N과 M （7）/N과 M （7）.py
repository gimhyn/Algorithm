import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
path = []

def combi():
    if len(path) == M:
        print(*path)
        return
        
    for i in range(N):
        path.append(nums[i])
        combi()
        path.pop()

combi()