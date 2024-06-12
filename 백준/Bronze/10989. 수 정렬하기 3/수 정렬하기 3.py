import sys

input = sys.stdin.readline
N = int(input())
numbers = [0]*10001

for i in range(N):
    numbers[int(input())] += 1

for num, count in enumerate(numbers):
    for _ in range(count):
        print(num)