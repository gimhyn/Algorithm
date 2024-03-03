arr = list([0]*100 for _ in range(100))
# 색종이 10*10
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    for r in range(a, a+10):
        for c in range(90 - b, 100 - b):
            arr[r][c] = 1

ans = 0
for j in range(100):
    ans += sum(arr[j])

print(ans)