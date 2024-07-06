import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input()) #달팽이 크기

    #달팽이를 그리기 위해 리스트를 미리 준비
    snail =
    col = 0
    num = 1
    snail[row][col] = num

    while num < n*n: #채워지는 숫자만큼 반복
        #이동할 위치가 달팽이 범위 내에 있는지 확인
        nr = row + dr[direct]
        nc = col + dc[direct]

        if 0 <= nr < N and 0 <= nc < N: #이동하려는 방향이 범위 내인지 확인
            #값이 비어 있는지 확인
            if snail[nc][nr] == 0:
                num += 1
                row = nr
                col = nc
                snail[row][col] = num
            else:
                direct = (direct + 1) % 4 #방향 범위 맞추기 위함
        else:
            direct = (direct+1)%4

    print(f'#{tc}')
    for row in range(n):
        print(*snail[row])