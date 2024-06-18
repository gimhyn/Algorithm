import sys
from collections import Counter

input = sys.stdin.read
data = list(map(int, input().strip().split()))

N = data[0]
numbers = data[1:]

# 산술평균
mean = round(sum(numbers) / N)

# 중앙값 계산
sorted_numbers = sorted(numbers)
median = sorted_numbers[N // 2]

# 최빈값 계산
frequency = Counter(numbers)
modes = frequency.most_common()
modes.sort(key=lambda x: (-x[1], x[0]))

if len(modes) > 1 and modes[0][1] == modes[1][1]:
    mode = modes[1][0]
else:
    mode = modes[0][0]

# 범위 계산
range_value = max(numbers) - min(numbers)

# 결과 출력
print(mean)
print(median)
print(mode)
print(range_value)
