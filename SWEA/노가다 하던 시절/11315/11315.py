# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input() for _ in range(N))
    flag = 1
    for r in range(N):
        if not flag:
            break
        for c in range(N):
            dr = [-2, -1, 0, 1, 2]
            dc = [-2, -1, 0, 1, 2]
            cnt_r = cnt_c = cnt_v1 = cnt_v2 = 0
            for i in range(5):
                nr = r+dr[i]
                nc = c+dc[i]
                if 0 <= nr < N:
                    if arr[nr][c] == 'o':
                        cnt_r += 1
                    if 0 <= nc < N and arr[nr][nc] == 'o':
                        cnt_v1 += 1
                    if 0 <= c+dc[4-i] < N and arr[nr][c+dc[4-i]] == 'o':
                        cnt_v2 += 1
                if 0 <= nc < N and arr[r][nc] == 'o':
                    cnt_c += 1

            if cnt_r >= 5 or cnt_c >= 5 or cnt_v1 >= 5 or cnt_v2 >=5:
                print(f'#{tc} YES')
                flag = 0
                break
    else:
        print(f'#{tc} NO')


