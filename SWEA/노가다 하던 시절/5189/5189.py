import sys
sys.stdin = open('5189_input.txt')

def dfs(i, s, cur):             # 시작점, 누적합, 현재위치
    global ans
    if ans <= s:        # 답보다 크면
        return          # 더 안 볼게요

    if i == N:
        # 여태까지 소모량 + 출발지로 복귀 비용
        ans = min(ans, s+arr[cur][1])
        return
    for j in range(2, N+1):
        if visited[j] == 0:
            visited[j] = 1
            dfs(i+1, s + arr[cur][j], j)
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * (N + 1)] + list([0] + list(map(int, input().split())) for _ in range(N))
    ans = 100 * N
    visited = [0]*(N+1)
    # 출발지 무조건 1, 복귀도 1로
    dfs(1, 0, 1)
    print(f'#{tc} {ans}')
