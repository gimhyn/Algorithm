# import sys
# sys.stdin = open('sample_input.txt')

def get_count(i, s):
    global cnt
    if i == N:              # 끝까지 다 결정했고
        if s == K:          # 누적합이 K면
            cnt += 1        # 카운트 올립니다
        return
    get_count(i+1, s+nums[i])   # nums[i]를 포함하는 경우
    get_count(i+1, s)           # nums[i]를 포함하지 않는 경우

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))      # 숫자 받기
    cnt = 0
    get_count(0, 0)

    print(f'#{tc} {cnt}')