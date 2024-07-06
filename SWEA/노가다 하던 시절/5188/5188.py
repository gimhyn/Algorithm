import sys
sys.stdin = open('5188_input.txt')
from collections import deque

def findroute(start, end):
    global m
    dr = [0, 1]
    dc = [1, 0]
    r = start
    c = start
    visited[r][c] = arr[r][c]
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if start <= nr <= end and start <= nc <= end and not visited[nr][nc]:
                q.append((r, c))
                visited[nr][nc] = visited[r][c] + arr[nr][nc]
                r, c = nr, nc
                if nr == end and nc == end:
                    if m > visited[nr][nc]:
                        m = visited[nr][nc]
    return


# 한 번 간 데 또 못가니까 잘못된 건 알겠지만 어케 고침요 ㅠ



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    m = 1023    # 최솟값 받을 변수
    visited = list([0]*N for __ in range(N))
    findroute(0, N-1)
    print(f'#{tc} {m}')
