import sys
input = sys.stdin.readline 

t = int(input())

for tc in range(t):
    a, b = map(int, input().split())
    print(pow(a, b, 10) if pow(a, b, 10) != 0 else 10)
