import sys
from itertools import combinations
input = sys.stdin.readline

def find_min(M, now):
    res = []

    if M == now:
        for r in distance:
            res.append(min(r))  # 각 집에서 가장 가까운 치킨 집의 거리 추가
        return sum(res)  # 모든 집에 대해 가장 가까운 치킨집까지의 거리 합산

    # M개의 치킨집을 고르기 위한 조합을 만들고 그 조합에 대해 계산
    min_distance = sys.maxsize  # 매우 큰 값으로 초기화
    for comb in combinations(range(len(chickens)), M):
        temp_distance = 0
        for i in range(len(houses)):
            # 현재 집에서 선택된 치킨집까지의 최소 거리 구하기
            temp_distance += min(distance[i][j] for j in comb)
        
        min_distance = min(min_distance, temp_distance)  # 최소 거리 갱신

    return min_distance

n, m = map(int, input().split())
chickens = []
houses = []
town = []

r = 0
for i in range(n):
    row = list(map(int, input().split()))

    for idx, char in enumerate(row):
        if char == 1:
            houses.append((r, idx))
        elif char == 2:
            chickens.append((r, idx))

    town.append(row)
    r += 1

# 0: 빈칸, 1: 집, 2: 치킨집
# 거리는 abs(r1-r2) + abs(c1-c2)

distance = [[0] * len(chickens) for _ in range(len(houses))]

for i in range(len(houses)):
    for j in range(len(chickens)):
        distance[i][j] = abs(houses[i][0] - chickens[j][0]) + abs(houses[i][1] - chickens[j][1])

print(find_min(m, len(chickens)))
