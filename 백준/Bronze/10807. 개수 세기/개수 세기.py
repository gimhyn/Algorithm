import sys
input = sys.stdin.readline 

N = int(input())
nums = list(map(int, input().split()))
target = int(input())

print(nums.count(target))