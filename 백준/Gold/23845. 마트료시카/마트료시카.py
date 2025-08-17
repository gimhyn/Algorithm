import sys
from heapq import heappop, heappush

n = int(input())
dolls = list(map(int, input().strip().split()))
now = dict()

for x in dolls:
    if x not in now:
        now[x] = 1
    else:
        now[x] += 1

now = sorted(list(now.items()))
m = len(now)
for i in range(m):
    now[i] = list(now[i])

res = 0
while m != 0:
    cnt = 0
    for i in range(m):
        if i != m -1 and now[i][0] + 1 == now[i+1][0]:
            if cnt > 0:
                cnt += 1
            else:
                cnt += 2
        else:
            if not cnt:
                res += now[i][0] * now[i][1]
                now[i][1] = 0
            else:
                go = now[i][0]
                now[i][1] -= 1
                idx = i -1
                for k in range(cnt -1):
                    now[idx-k][1] -= 1
                res += go * cnt
                cnt = 0

    idx = 0
    while idx < len(now):
        if now[idx][1] == 0:
            del now[idx]
        else:
            idx += 1
    m = len(now)
print(res)

