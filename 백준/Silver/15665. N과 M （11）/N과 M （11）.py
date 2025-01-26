import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []
res = set()

def sequence(depth):
    if depth == M:
        ans_str = str(ans)
        if ans_str in res:
            return
        else:
            print(*ans)
            res.add(ans_str)
            return

    for i in range(N):
        ans.append(nums[i])
        sequence(depth+1)
        ans.pop()

sequence(0)