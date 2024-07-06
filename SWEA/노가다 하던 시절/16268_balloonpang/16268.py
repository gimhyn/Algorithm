import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    dr = [-1, 1, 0, 0]     # 상하좌우
    dc = [0, 0, -1, 1]
    max_confetti = 0
    for r in range(N):
        for c in range(M):
            s = arr[r][c]              # 중앙값
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    s += arr[nr][nc]
            if max_confetti < s:
                max_confetti = s

    print(f'#{tc} {max_confetti}')