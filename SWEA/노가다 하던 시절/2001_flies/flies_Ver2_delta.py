import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    dr = []
    dc = []
    for i in range(M):
        for j in range(M):
            dr.append(i)
            dc.append(j)

    max_flies = 0
    for r in range(N):
        for c in range(N):
            sum_flies = 0
            for k in range(M*M):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    sum_flies += arr[nr][nc]

            if max_flies < sum_flies:
                max_flies = sum_flies

    print(f'#{tc} {max_flies}')