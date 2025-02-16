import sys
import math
input = sys.stdin.readline

def is_available(x):
    for row in range(x):
        if abs(row - x) == abs(used_row[row] - used_row[x]):
            return False
    return True


def solution(x):
    global ans
    if x == N:
        ans += 1
        return

    for col in range(N):
        if not used_col[col]:
            used_row[x] = col
            used_col[col] = 1

            if is_available(x):
                solution(x+1)

            used_col[col] = 0

N = int(input())
used_row = [0] * N # 각 행 몇 번째 열에 놓았는가?
used_col = [0] * N
ans = 0
solution(0)
print(ans)
