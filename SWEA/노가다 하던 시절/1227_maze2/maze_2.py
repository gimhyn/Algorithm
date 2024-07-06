import sys
sys.stdin = open('input.txt')

def findroute(arr, n, start, goal):
    q = []          # 큐 생성
    visited = [[0]*n for _ in range(n)]    # 방문 처리
     # 길 차례로 방문
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]  # 상하좌우
    r, c = start
    q.append([r, c])    # 시작점 인큐
    visited[r][c] = 1   # 시작점 방문처리
    while q:
        r, c =  q.pop(0)        #디큐
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0 <= nr < n and 0 <= nc < n:   # 미로 안이고
                if [nr, nc] == goal:            # 도착
                    return 1     # visited[goal]-2
                elif arr[nr][nc] == 0 and visited[nr][nc] == 0: # 안 가본 길이 있으면?
                    q.append([nr, nc])
                    visited[nr][nc] = visited[r][c] + 1     # 거기 가는데 얼마나 걸리죠?
    return 0

T = 10

for tc in range(1, T+1):
    tc_n = input()
    # 1:벽, 0:길, 2:출발, 3:도착
    N = 100
    maze = list(list(map(int, input().strip())) for _ in range(N))

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                s = [r, c]
            elif maze[r][c] == 3:
                g = [r, c]

    print(f'#{tc} {findroute(maze, N, s, g)}')
