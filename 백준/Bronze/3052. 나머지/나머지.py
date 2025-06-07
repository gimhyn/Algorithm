import sys
input = sys.stdin.readline

res= set()
for i in range(10):
    num = int(input())
    res.add(num % 42)
    
print(len(res))