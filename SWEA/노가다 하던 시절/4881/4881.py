import sys
sys.stdin = open('4881_input.txt')

def f(i, k, s):
    global min_v
    if i == k:
        if min_v > s:   # 합이 최솟값보다 작다면 최솟값 갱신
            min_v = s
    elif s >= min_v:    # 만일 지금까지 구한 합이 최솟값보다 크다면
        return          # 더 구할 필요 없음
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i] # 자기 자리부터 차례대로 옆자리랑 바꾸기
            f(i+1, k, s+arr[i][p[i]])   #합 갱신.........
            p[i], p[j] = p[j], p[i] # 다시 바꾸기 전 원래 자리로 복구



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    min_v = 90 # 가능한 최대치
    p = [i for i in range(N)]   # 각 행에서 고른 열 저장할 배열
    f(0, N, 0)

    print(f'#{tc} {min_v}')