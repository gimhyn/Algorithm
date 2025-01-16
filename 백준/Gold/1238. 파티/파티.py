import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    """시작 노드에서 모든 노드까지의 최단 거리를 계산하는 함수"""
    distance = [float('inf')] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for cost, neighbor in graph[now]:
            new_cost = dist + cost
            if distance[neighbor] > new_cost:
                distance[neighbor] = new_cost
                heapq.heappush(q, (new_cost, neighbor))

    return distance

# 입력 처리
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    src, dest, time = map(int, input().split())
    graph[src].append((time, dest))

# x에서 각 노드로 가는 최단 거리 계산
from_x = dijkstra(x)

# 각 노드에서 x로 가는 최단 거리 계산
to_x = [0] * (n + 1)
for i in range(1, n + 1):
    if i != x:  # 자기 자신에서 출발할 필요 없음
        to_x[i] = dijkstra(i)[x]

# 왕복 거리 계산 및 최대값 출력
max_cost = max(from_x[i] + to_x[i] for i in range(1, n + 1))
print(max_cost)
