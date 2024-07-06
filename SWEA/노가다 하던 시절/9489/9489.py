import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, 2):
    N, M = map(int, input().split())
    data = list(list(input().split()) for _ in range(N))
    print(data)
    #  빈 땅 : 0, 구조물 : 1
    max_len = 0
    for r in range(N):
        print(data[r].split('0'))

