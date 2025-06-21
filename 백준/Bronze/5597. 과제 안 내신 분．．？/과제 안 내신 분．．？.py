import sys
input = sys.stdin.readline

students = set(i for i in range(1, 31))
goods = set(int(input()) for _ in range(28))

bads = sorted(students - goods)
for bad in bads:
    print(bad, end='\n')
   