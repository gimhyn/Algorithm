import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

def bfs(start, target):
    q = deque([(0, start)])
    visited = [0] * 100001

    res, min_turn = 0, 100001
    while q:
        turn, now = q.popleft()
        dx = [1, -1, now]

        if now == target:
            if min_turn > turn:
                min_turn = turn
                res = 1
                continue
            elif min_turn == turn:
                res += 1
            else:
                continue

        for i in range(3):
            next = now + dx[i]
            if 0 <= next <= 100000 and (not visited[next] or visited[next] > turn):
                q.append((turn+1, next))
                visited[next] = turn + 1

    return min_turn, res

if N == K:
    print(0)
    print(1)
else:
    mt, cnt = bfs(N, K)
    print(mt)
    print(cnt)