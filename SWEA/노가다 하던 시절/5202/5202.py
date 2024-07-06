import sys
sys.stdin = open('5202_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(list(map(int, input().split())) for _ in range(N))
    # 화물차 작업 시간 s / 종료시간 e
    new_lst = sorted(lst, key = lambda x: (x[1], x[1]-x[0])) # 종료 시간 빠른 순 -> 같으면 소요 시간 짧은 순으로 정렬
    cnt = 0
    end = 0 # 시작점 설정

    for truck in new_lst:
        if truck[0] >= end:     # 만약 해당 화물차의 시작 시간이 전 트럭의 종료 시간 이후라면
            cnt += 1            # 작업 가능
            end = truck[1]      # 끝나는 시간 갱신
    print(f'#{tc} {cnt}')