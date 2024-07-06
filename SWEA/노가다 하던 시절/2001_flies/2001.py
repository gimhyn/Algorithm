import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    max_flies = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            s = 0
            for i in range(M):
                for j in range(M):
                    s += arr[r+i][c+j]

            if max_flies < s:
                max_flies = s

    print(f'#{tc} {max_flies}')