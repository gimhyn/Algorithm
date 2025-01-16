import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, n):
    distance = list([float('inf')] * n for _ in range(n))
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        cost, x, y = heapq.heappop(q)
        if distance[x][y] < cost:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                total_cost = cost + graph[nx][ny]
                if distance[nx][ny] > total_cost:
                    distance[nx][ny] = total_cost
                    heapq.heappush(q, (total_cost, nx, ny))

    return distance[n-1][n-1]

tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = list(list(map(int, input().split())) for _ in range(N))
    ans = dijkstra(board, N)
    print(f'Problem {tc}: {ans}')
    tc += 1