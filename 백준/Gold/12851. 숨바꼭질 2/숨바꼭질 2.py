import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

def bfs(start, target):
    q = deque([start])
    visited = [0] * 100001

    res, min_turn = 0, 100001
    while q:
        now = q.popleft()
        turn = visited[now]
        dx = [1, -1, now]

        if now == target:
            res += 1
            min_turn = turn

        for i in range(3):
            next = now + dx[i]
            if 0 <= next <= 100000 and (not visited[next] or visited[next] > turn):
                q.append(next)
                visited[next] = turn + 1

    return min_turn, res

if N == K:
    print(0)
    print(1)
else:
    mt, cnt = bfs(N, K)
    print(mt)
    print(cnt)