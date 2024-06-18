import sys
from collections import Counter

# 입력
input = sys.stdin.read
data = input().strip().split()

N = int(data[0])
numbers = list(map(int, data[1:]))

# 산술평균
mean = round(sum(numbers) / N)

# 중앙값
sorted_numbers = sorted(numbers)
median = sorted_numbers[N // 2]

# 최빈값
counter = Counter(numbers)
most_common = counter.most_common()
most_common.sort(key=lambda x: (-x[1], x[0]))

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    mode = most_common[1][0]
else:
    mode = most_common[0][0]

# 범위
range_value = max(numbers) - min(numbers)

# 출력
print(mean)
print(median)
print(mode)
print(range_value)
