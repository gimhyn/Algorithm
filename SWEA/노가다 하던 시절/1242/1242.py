import sys
sys.stdin = open('sample_input.txt')

def valid(code):
    s = 0
    cnt = 0
    res = 0
    while code > 0:
        if cnt % 2 == 0:
            s += code % 10
            res += code % 10
            code //= 10
            cnt += 1
        else:
            s += (code % 10)*3
            res += code % 10
            code //= 10
            cnt += 1
    if s % 10 == 0:
        return res
    else:
        return 0

def findcode(arr):
    cnt = 0
    codes = []
#16진수 -> 2진수: 숫자 하나당 4자리
#그런데 암호코드 56*n ; 14*n 개의 16진수 필요함
    for r in range(N):
        for c in range(M-1, -1, -1):
            if arr[r][c] != '0':
                codes.append(arr[r][c-14i:c])






#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 세로 2000, 가로 500 이하