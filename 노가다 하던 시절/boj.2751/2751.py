import sys
N = int(input())
lst = list(int(sys.stdin.readline()) for _ in range(N))
lst.sort()
print(*lst, sep='\n')