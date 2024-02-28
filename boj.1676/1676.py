N = int(input())

count = 0

f = N
while N > 1:
    f *= (N-1)
    N -= 1
    if f % 10 == 0:
        count += 1
        f //= 10

print(count)