from collections import deque

T = int(input())
for tc in range(T):
    pq = deque()
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    for i in range(N):
        pq.append([priorities[i], i])

    priorities.sort(reverse=True)
    cnt = 0
    while pq:
        if pq[0][0] == priorities[0]:
            cnt += 1
            out = pq.popleft()
            if out[1] == M:
                print(cnt)
                break
            priorities.pop(0)
        else:
            pq.rotate(-1)