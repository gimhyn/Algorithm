def findquarter(tar, row, col):
    global order
    half = tar // 2
    if tar == 1:
        return 
    if  row < half:
        if col < half:
            findquarter(half, row, col)
        else:
            order += half ** 2
            findquarter(half, row, col-half)
    else:
        if col < half:
            order += half ** 2 * 2
            findquarter(half, row-half, col)
        else:
            order += half **2 * 3
            findquarter(half, row-half, col-half)

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
# N, r, c 정수  1<= N <=15

order = 0
findquarter(2**N, r, c)
print(order)