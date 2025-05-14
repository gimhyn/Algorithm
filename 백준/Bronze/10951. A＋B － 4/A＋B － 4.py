import sys

for line in sys.stdin.read().splitlines():
    a, b = map(int, line.split())
    print(a+b)    