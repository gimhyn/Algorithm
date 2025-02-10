import sys
import heapq
input = sys.stdin.readline

def bfs(start, goal):
    dist = [float('inf')] * 100001
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        time, now = heapq.heappop(pq)
        if dist[now] < time:
            continue

        d = [-1, 1, now]
        t = [1, 1, 0]
        for i in range(3):
            next = now + d[i]
            dis = time + t[i]
            if 0 <= next < 100001 and dist[next] > dis:
                dist[next] = dis
                pq.append((dis, next))

    return dist[goal]

N, K = map(int, input().split())
print(bfs(N, K))