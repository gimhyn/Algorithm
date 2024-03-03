C, R = map(int, input().split())
K = int(input())
seat = [1, 1]
arr = list([0]*R for _ in range(C))

turn = 0
dr = [0, 1, 0, -1] # 우 하 좌 상
dc = [1, 0, -1, 0]

r = c = 0       # 초기값 세팅
arr[r][c] = 1
num = 1
if K > R*C:
    print(0)

else:
    while num < R*C:
        nr = r + dr[turn % 4]
        nc = c + dc[turn % 4]
        if 0 <= nr < C and 0 <= nc < R and not arr[nr][nc]:
            num += 1
            arr[nr][nc] = num
            r = nr
            c = nc
        else:
            turn += 1

        if num == K:
            seat = [r+1, c+1]
            break
    print(*seat)