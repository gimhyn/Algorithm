import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
path = []

def combi(depth):
    if depth == M:
        print(*path)
        return
        
    for i in range(N):
        if path and nums[i] < path[-1]:
            continue
        path.append(nums[i])
        combi(depth+1)
        path.pop()

combi(0)