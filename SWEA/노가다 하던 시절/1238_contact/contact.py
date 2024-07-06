import sys
sys.stdin = open('input.txt')

def bfs(arr, s):
    q = []                  # 큐 생성
    got_call = [0]*101      # 연락 받은 순서 기록
    begin = s               # 시작점 지정
    q.append(begin)         # 시작점 인큐
    got_call[begin] = 1     # 확인 리스트 값 바꿔주기

    while q:
        begin = q.pop(0)                            # 디큐
        for i in arr[begin]:
            if got_call[i] == 0:                    # 아직 전화 못 받은 친구라면
                q.append(i)                         # 인큐
                got_call[i] = got_call[begin] + 1   # 몇 번째로 전화 받는지 기록

    # 연락 다 돌렸으면 가장 마지막에 연락 받은 사람 찾기
    last = 0    # 누가 가장 마지막?
    num = 1     # 몇 번째로 받음?
    for j in range(1, 101):
        if got_call[j] > num:
            num = got_call[j]
            last = j
        elif got_call[j] == num:
            if last < j:
                last = j
    return last

T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    input_list = list(map(int, input().split()))
    contacts = [[]*101 for _ in range(101)]      # 비상연락망

    for i in range(N//2):
        me, friend = input_list[2*i], input_list[2*i+1]
        if friend not in contacts[me]:          # 중복 방지
            contacts[me].append(friend)

    print(f'#{tc} {bfs(contacts, start)}')