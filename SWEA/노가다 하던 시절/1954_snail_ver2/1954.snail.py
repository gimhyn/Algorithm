# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)] #빈 배열 만들기
    #우->하->좌->상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    num = 1
    r = 0
    c = 0
    i = 0
    snail[r][c] = num

    while num < N*N: #범위 확인
        r += dr[i]
        c += dc[i]
        if 0 <= r < N and 0 <= c < N and snail[r][c] == 0:
            num += 1
            snail[r][c] = num
        else:
            r -= dr[i]
            c -= dc[i]
            i = (i+1) % 4

    print(f'#{tc}')
    for j in range(N):
        print(*snail[j])

