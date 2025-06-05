import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    h, w, n = map(int,input().split())

    res = 100 * (n % h if n % h else h)
    res += (n//h + 1) if n % h else (n//h)
    print(res)