import sys
sys.stdin = open('4831_input.txt')

T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split()) #n번 정류장(종점)/  k:최대 거리/ m:충전기개수
    m_list = list(map(int, input().split())) #충전기 위치

    #시작 지점 0

    answer = -1
    for i in range(m-1):
        if m_list[0] > k:
            answer = 0
            break
        elif m_list[i+1] - m_list[i] > k:
            answer = 0
            break

    if answer != 0: #일단 무조건 갈 수 있는 상태
        cnt = 0
        charge_point = 0
        if



    #종점 못 가면 0 리턴
    print(f'#{tc} {answer}')