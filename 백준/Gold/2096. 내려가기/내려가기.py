import sys
input = sys.stdin.readline

n = int(input())
prev_max = list(map(int, input().split()))
prev_min = prev_max[:]

# 두 번째 행부터 계산
for _ in range(1, n):
    board = list(map(int, input().split()))
    
    # 현재 행에서 최댓값과 최솟값을 계산
    current_max = [
        board[0] + max(prev_max[0], prev_max[1]),
        board[1] + max(prev_max),
        board[2] + max(prev_max[1], prev_max[2])
    ]
    current_min = [
        board[0] + min(prev_min[0], prev_min[1]),
        board[1] + min(prev_min),
        board[2] + min(prev_min[1], prev_min[2])
    ]
    
    # 이전 행을 덮어쓰기
    prev_max = current_max
    prev_min = current_min

# 결과 출력
print(max(prev_max), min(prev_min))
