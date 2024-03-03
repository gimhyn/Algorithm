N = int(input())
nums = list(map(int, input().split()))
increasing = 1
decreasing = 1
max_len = 1

for i in range(1, N):
    if nums[i] >= nums[i-1]:
        increasing += 1
        if max_len < increasing:
            max_len = increasing
    else:
        increasing = 1            # 값 초기화

    if nums[i] <= nums[i-1]:
        decreasing += 1
        if max_len < decreasing:
            max_len = decreasing
    else:
        decreasing = 1

print(max_len)