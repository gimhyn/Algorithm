import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

res = []
visited = [0] * N
def sequence(depth, index):
    if depth == M:
        print(' '.join(map(str, res)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            res.append(i+1)
            sequence(depth+1, i)
            visited[i] = 0
            res.pop()

sequence(0, 0)