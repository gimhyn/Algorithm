def can_make_cables(cables, required_cables, length):
    count = 0
    for cable in cables:
        count += cable // length
    return count >= required_cables

def find_max_length(cables, required_cables):
    low, high = 1, max(cables)
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if can_make_cables(cables, required_cables, mid):
            result = mid  # 이 길이로 만들 수 있으므로 결과를 갱신
            low = mid + 1  # 더 긴 길이도 가능한지 탐색
        else:
            high = mid - 1  # 짧아야 하는 경우 범위를 줄임
    return result

# 입력 처리
import sys
K, N = map(int, sys.stdin.readline().split())
cables = list(int(sys.stdin.readline()) for _ in range(K))

# 최대 랜선 길이 찾기
max_length = find_max_length(cables, N)
print(max_length)
