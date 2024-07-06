import sys
sys.stdin = open('5099_input.txt')

from collections import deque
import sys

sys.stdin = open('5099_input.txt')

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # n개의 화덕 m개의 피자
    pizza = list(map(int, input().split()))
    oven = deque()
    idx = 0
    for i in range(N):
        oven.append([i + 1, pizza[i]])  # 첫 한 바퀴
        idx += 1

    p_cnt = 0
    while p_cnt < N - 1:
        for j in range(N):  # 화덕 돌리기
            oven[j][1] //= 2
            if oven[j][1] == 0:
                if idx < M:
                    oven[j] = [idx + 1, pizza[idx]]
                    idx += 1
                else:
                    oven[j] = [-1, -1]
                    p_cnt += 1
                    if p_cnt == N - 1:
                        break
    while len(oven) > 1:
        for k in range(N):
            if oven[0][0] == -1:
                oven.popleft()
        for k in range(N):
            if oven[0][0] == -1:
                oven.popleft()

    print(f'#{tc} {oven[0][0]}')


