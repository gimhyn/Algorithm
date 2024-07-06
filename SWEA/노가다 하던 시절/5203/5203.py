# import sys
# sys.stdin = open('5203_input.txt')

def babygin(arr, p):
    global winner
    if len(arr) >= 3:
        arr.sort()                      # 일단 정렬 갈겨줍니다
        print(arr)
        for i in range(len(arr)-2):     # 앞부터 돌 건데요
            if arr[i] == arr[i+1] and arr[i] == arr[i+2]:  # triplet 되나 확인
                winner = p          # 위너 갱신
                return              # 끝
            else:
                if arr[i]+1 in arr and arr[i]+2 in arr:
                    winner = p                  # run이면 winner 갱신
                    return                      # 끝


T = int(input())
for tc in range(1):
    ipt = list(map(int, input().split()))
    cards_1 = []
    cards_2 = []
    print(f'#{tc}', end = ' ')
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            cards_1.append(ipt[i])
            babygin(cards_1, 1)
        else:
            cards_2.append(ipt[i])
            babygin(cards_2, 2)
        if winner:                          # 만약 승자 정해졌다면?
            print(winner)                   # 출력하고
            break                           # 끝내줍니다

    if not winner:
        print(winner)