import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
cleaner = 0

for i in range(r):
    if room[i][0] == -1:
        cleaner = i
        break

def spread():
    temp = [[0] * c for _ in range(r)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for row in range(r):
        for col in range(c):
            if room[row][col] > 0:
                dust = room[row][col] // 5
                cnt = 0
    
                for i in range(4):
                    nr = row + dr[i]
                    nc = col + dc[i]
                    if 0 <= nr < r and 0 <= nc < c and room[nr][nc] != -1:
                        cnt += 1
                        temp[nr][nc] += dust
    
                room[row][col] -= cnt * dust

    for row in range(r):
        for col in range(c):
            room[row][col] += temp[row][col]

    return

def clean():
    upper, lower = cleaner, cleaner +1

    # 위쪽 역방향
    for row in range(upper-1, 0, -1):
        room[row][0] = room[row-1][0]
    for col in range(c-1):
        room[0][col] = room[0][col+1]
    for row in range(upper):
        room[row][c-1] = room[row+1][c-1]
    for col in range(c-1, 1, -1):
        room[upper][col] = room[upper][col-1]
    room[upper][1] = 0

    # 아래쪽
    for row in range(lower+1, r-1):
        room[row][0] = room[row+1][0]
    for col in range(c-1):
        room[r-1][col] = room[r-1][col+1]
    for row in range(r-1, lower, -1):
        room[row][c-1] = room[row-1][c-1]
    for col in range(c-1, 1, -1):
        room[lower][col] = room[lower][col-1]
    room[lower][1] = 0

    return

for sec in range(t):
    spread()
    clean()

print(2 + sum(sum(x) for x in room))