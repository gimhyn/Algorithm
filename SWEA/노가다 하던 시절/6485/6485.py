# import sys
# sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    n =int(input()) #버스 노선 수 / 1<= n <= 500
    ab_list = list(list(map(int, input().split())) for _ in range(n))
    #1 <= a <= b <= 5000

    p = int(input()) #1<= p <= 500
    c_list = list(int(input()) for _ in range(p)) #정류장 번호 담은 리스트

    arr = [0]*5001 #정류장 번호 인덱스에 다니는 버스 담기

    for idx in range(n):
        a, b = ab_list[idx][0], ab_list[idx][1]
        for i in range(a, b+1):
            arr[i] += 1

    answer = []


    for j in range(p):
        answer.append(arr[c_list[j]])

    print(f'#{tc}', *answer)
