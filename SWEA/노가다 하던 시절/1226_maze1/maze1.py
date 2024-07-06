# import sys
# sys.stdin = open('input.txt')

def findroute(arr, start, goal):
    q = []          # 큐 생성
    visited = [[0]*16 for _ in range(16)]    # 방문 처리
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
            if 0 <= nr < 16 and 0 <= nc < 16: # 미로 안이고
                if [nr, nc] == goal:
                    return 1        # 도착
                elif arr[nr][nc] == 0 and visited[nr][nc] == 0: # 안 가본 길이 있으면?
                    q.append([nr, nc])
                    visited[nr][nc] = visited[r][c] + 1     # 거기 가는데 얼마나 걸리죠?
    return 0

T = 10
for t in range(1, T+1):
    tc = input()
    # 1:벽, 0:길, 2:출발, 3:도착
    maze = list(list(map(int, input().strip())) for _ in range(16))

    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                s = [r, c]
            elif maze[r][c] == 3:
                g = [r, c]

    print(f'#{tc} {findroute(maze, s, g)}')
