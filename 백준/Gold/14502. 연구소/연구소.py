import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
lab = []
virus = []
cand = []

for row in range(N):
    temp = list(map(int, input().split()))
    for col in range(M):
        if temp[col] == 2:
            virus.append((row, col))
        elif temp[col] == 0:
            cand.append((row, col))
    lab.append(temp)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(candidates):
    q = deque(virus)
    # 이차원 배열 깊은 복사 주의
    temp_lab = [x[:] for x in lab]
    for w in candidates:
        temp_lab[w[0]][w[1]] = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not temp_lab[nr][nc]:
                temp_lab[nr][nc] = 2
                q.append((nr, nc))

    cnt = sum(row.count(0) for row in temp_lab)
    return cnt



walls = list(combinations(cand, 3))
safe = 0
for combi in walls:
    safe = max(safe, bfs(combi))

print(safe)