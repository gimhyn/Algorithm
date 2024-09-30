import sys
import heapq

input = sys.stdin.readline


N = int(input())
classes = []

for i in range(N):
    s, t= map(int, input().strip().split())
    classes.append((s, t))


classes.sort()

min_heap = []

for start, end in classes:
    if min_heap and min_heap[0] <= start:
        heapq.heappop(min_heap)
    
    heapq.heappush(min_heap, end)
    
print(len(min_heap))