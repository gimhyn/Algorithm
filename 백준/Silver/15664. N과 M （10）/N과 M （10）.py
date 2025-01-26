import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []
res = set()
visited = [0] * N

def sequence(depth):
    if depth == M:
        ans_str = str(ans)
        if ans_str in res:
            return
        else:
            print(*ans)
            res.add(ans_str)
            return

    for i in range(depth, N):
        if visited[i]:
            continue
        elif ans and ans[-1] > nums[i]:
            continue
        visited[i] = 1
        ans.append(nums[i])
        sequence(depth+1)
        ans.pop()
        visited[i] = 0
    

sequence(0)