import sys
input = sys.stdin.readline 

t = int(input())

for tc in range(t):
    a, b= map(int, input().split())
    print(a+b)