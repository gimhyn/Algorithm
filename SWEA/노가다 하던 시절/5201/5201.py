# import sys
# sys.stdin = open('5201_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight_list = list(map(int, input().split()))
    truck_list = list(map(int, input().split()))

    weight_list.sort(reverse=True)  # 무거운 순으로 정렬합니다
    truck_list.sort(reverse=True)
    heavy = 0                       # 무게 누적합
    idx = 0
    for weight in weight_list:
        if idx >= M:                # 만약 모든 트럭 다 썼다면
            break                   # break
        if weight <= truck_list[idx]:   # 만약 적재 가능한 무게면
            heavy += weight             # 누적합 갱신
            idx += 1                    # 트럭 인덱스 갱신

    print(f'#{tc} {heavy}')