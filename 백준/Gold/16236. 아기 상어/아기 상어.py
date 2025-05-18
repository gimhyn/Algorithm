import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# 해당 포인트에서 가장 가까운 물고기 찾기
def bfs(r, c):
    global size

    visited = [[0] * n for _ in range(n)]
    q = deque([(r,c)])
    visited[r][c] = 1
    fish = []

    while q:
        cr, cc = q.popleft()
        if fish and fish[0][0] < visited[cr][cc]:
            continue

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                # 일단 최단 거리 방문 처리(못 감, 갈 수 있으나 못 먹음, 갈 수 있고 먹을 수 있음)
                visited[nr][nc] = visited[cr][cc] + 1
                if 0 <= arr[nr][nc] <= size[0]: # 갈 수 있음
                    q.append((nr, nc))
                    if 0 < arr[nr][nc] < size[0]:
                        fish.append((visited[cr][cc], nr, nc))

    return sorted(fish, key=lambda x : (x[0], x[1], x[2]))


# 물고기 먹기
def eat_fish(r, c):
    global size, time

    while True:
        fish = bfs(r, c)

        if not fish:
            return time

        # 위치 갱신
        cnt, r, c = fish[0]
        time += cnt
        size[1] += 1
        arr[r][c] = 0
        # 먹은 물고기 위치 0으로

        if size[0] == size[1]:
            size[0] += 1
            size[1] = 0


n = int(input())
arr = []
size = [2, 0]
time = 0

for row in range(n):
    temp = list(map(int, input().split()))
    if 9 in temp:
        sr = row
        sc = temp.index(9)
        temp[sc] = 0

    arr.append(temp)

print(eat_fish(sr, sc))