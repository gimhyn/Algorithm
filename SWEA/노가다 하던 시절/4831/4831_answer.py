import sys
sys.stdin = open('4831_input.txt')

T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    # k: 이동 거리/n: 종점/m:개수
    station = set(map(int,input().split())) #list도 가능하지만 hash 덕분에 set이 조금 더 연산 빠름. 중복 없기에 set가능.

    #충전횟수 저장할 변수
    charge = 0
    #버스의 위치
    move = k #충전된 상태로 출발하므로
    #마지막 충전소 위치 저장하는 변수
    last = 0

    while move < n: #버스에 종점에 도착하거나 넘어갈 때까지 반복
        for _ in range(k): #k만큼 갔기 때문에 최대 k번 되돌아 옴
            if move in station: #이동한 거리에 충전소 있다면
                charge += 1
                break #뒤로 되돌아 갈 필요 없음
            move -= 1 #한 칸씩 뒤로 돌아가기

        if last == move: #되돌아 갔을 때, 마지막 충전소 위치까지 왔다면
            charge = 0 #종점까지 갈 수 없음
            break   #더 이상 이동하지 않고 while 반복 종료

        last = move #새롭게 찾은 충전소 위치를 갱신
        move += k #다음 충전소 찾기 위해 최대 이동

    print(f'#{tc} {charge}')