import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
path = []
used = [0] * N
res = set()

def combi(depth):
    if depth == M:
        if tuple(path) in res:
            return
        print(*path)
        res.add(tuple(path))
        return
        
    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        path.append(nums[i])
        combi(depth+1)
        path.pop()
        used[i] = 0

combi(0)
