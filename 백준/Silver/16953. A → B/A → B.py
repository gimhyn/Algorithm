import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

def bfs(start, cnt, target):
    q = deque([(start, cnt)])

    while q:
        num, cnt = q.popleft()
        if num > target:
            continue
        elif num == target:
            return cnt
        q.append((num * 2, cnt + 1))
        q.append((10 * num + 1, cnt + 1))

    return -1

print(bfs(A, 1, B))
